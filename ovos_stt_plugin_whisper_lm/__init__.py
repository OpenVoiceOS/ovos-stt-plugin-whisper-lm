from huggingface_hub import hf_hub_download

import torch
from ovos_plugin_manager.templates.stt import STT
from ovos_utils.log import LOG
from transformers import pipeline

import whisper_lm_transformers  # Required to register the new pipeline



class WhisperLMSTT(STT):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        model = self.config.get("model")
        lm_model = self.config.get("lm_model")
        lm_repo = self.config.get("lm_repo")
        lm_alpha = self.config.get("lm_alpha", 0.33582369)
        lm_beta = self.config.get("lm_beta", 0.68825565)
        lang = self.lang.split("-")[0]
        if not lm_model:
            if lang not in self.available_languages:
                raise ValueError(f"For pretrained models language must be in {self.available_languages}")
            lm_model = f"5gram-{lang}.bin"
            lm_repo = "HiTZ/whisper-lm-ngrams"
            if not model:
                model = f"zuazo/whisper-medium-{lang}"
        if not model:
            model = "openai/whisper-large-v3-turbo"

        LOG.debug(f"Using language model: {lm_model}")
        LOG.debug(f"Using whisper model: {model}")

        device = "cpu"
        if self.config.get("use_cuda"):
            if not torch.cuda.is_available():
                LOG.error("CUDA is not available, running on CPU. inference will be SLOW!")
            else:
                device = "cuda"

        if lm_repo:
            lm_model = hf_hub_download(repo_id=lm_repo, filename=lm_model)
        self.pipe = pipeline(
            "whisper-with-lm",
            model=model,
            lm_model=lm_model, # Provide a kenlm model path
            lm_alpha=lm_alpha,
            lm_beta=lm_beta,
            language="eu",
            device=device
        )

    def execute(self, audio, language=None):
        if language and language != "auto" and language.split("-")[0] != self.lang.split("-")[0]:
            raise ValueError(f"Whisper with LM does not support dynamic language, only {self.lang} supported")
        result = self.pipe(audio.get_wav_data())
        return result["text"]

    @property
    def available_languages(self) -> set:
        return {"gl", "es", "eu", "ca"}



if __name__ == "__main__":
    from ovos_stt_plugin_whisper_lm import WhisperLMSTT
    b = WhisperLMSTT({"lang": "eu"})

    from speech_recognition import Recognizer, AudioFile

    jfk = "/home/miro/PycharmProjects/whisper-lm-transformers/tests/data/audio.wav"
    with AudioFile(jfk) as source:
        audio = Recognizer().record(source)

    a = b.execute(audio)
    print(a)
