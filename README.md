## Description

This is an OpenVoiceOS STT plugin. It combines [Whisper-LM-transformers](https://github.com/hitz-zentroa/whisper-lm-transformers), KenLM, and large language models with Whisper ASR models from the Hugging Face library.

## Install

`pip install ovos-stt-plugin-whisper-lm`

> ⚠️ Only **python <=3.11** is supported by some of the dependencies.

## Models

[HiTZ](https://huggingface.co/HiTZ/whisper-lm-ngrams) provides pretrained n-gram models.

Each `lm_model` is built with the KenLM toolkit. It is based on n-gram statistics from large, domain-specific corpora. The available models are:

- Basque (eu): `5gram-eu.bin` (11G)
- Galician (gl): `5gram-gl.bin` (8.4G)
- Catalan (ca): `5gram-ca.bin` (20G)
- Spanish (es): `5gram-es.bin` (13G)

[Xabier Zuazo](https://huggingface.co/zuazo) also provides finetuned Whisper models for these languages.

Instead of an n-gram model, you can use a large language model such as [Latxa](https://huggingface.co/collections/HiTZ/latxa-65a697e6838b3acc53677304).

## Configuration

The example below uses the [HiTZ Basque KenLM model](https://huggingface.co/HiTZ/whisper-lm-ngrams). Adjust `lm_alpha`, `lm_beta`, and the other parameters to get the best results with your own models.

```json
  "stt": {
    "module": "ovos-stt-plugin-whisper-lm",
    "ovos-stt-plugin-whisper-lm": {
        "model": "zuazo/whisper-medium-eu",
        "lm_repo": "HiTZ/whisper-lm-ngrams",
        "lm_model": "5gram-eu.bin",
        "lm_alpha": 0.33582369,
        "lm_beta": 0.68825565,
        "use_cuda": true
    }
  }
```
> 💡 Set `lm_repo` only if you want to specify a specific filename in `lm_model`.

To use a large language model instead of an n-gram model:

```json
  "stt": {
    "module": "ovos-stt-plugin-whisper-lm",
    "ovos-stt-plugin-whisper-lm": {
        "model": "zuazo/whisper-medium-eu",
        "lm_model": "HiTZ/latxa-7b-v1.2",
        "lm_alpha": 2.73329396,
        "lm_beta": 0.00178595,
        "use_cuda": true
    }
  }
```
> ⚠️ Running large language models next to Whisper needs enough GPU memory.

## Credits

[TigreGotico](https://tigregotico.pt) developed this plugin for OpenVoiceOS under the [ILENIA](https://proyectoilenia.es) project.

![](img.png)

> The Ministerio para la Transformación Digital y de la Función Pública funded this plugin, and the Plan de Recuperación, Transformación y Resiliencia funded it through NextGenerationEU, within the [ILENIA](https://proyectoilenia.es) project, reference 2022/TL22/00215337.

![](img_1.png)

The Creative Commons Attribution 4.0 International License (CC BY 4.0) covers the pretrained n-gram models. You may use, modify, and distribute these models if you credit the original creators.

```
@misc{dezuazo2025whisperlmimprovingasrmodels,
      title={Whisper-LM: Improving ASR Models with Language Models for Low-Resource Languages}, 
      author={Xabier de Zuazo and Eva Navas and Ibon Saratxaga and Inma Hernáez Rioja},
      year={2025},
      eprint={2503.23542},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2503.23542}, 
}
```
