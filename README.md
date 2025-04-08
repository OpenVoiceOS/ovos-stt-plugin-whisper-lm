## Description

OpenVoiceOS STT plugin for [Whisper-LM-transformers](https://github.com/hitz-zentroa/whisper-lm-transformers), KenLM and Large language model integration with Whisper ASR models implemented in Hugging Face library.

## Install

`pip install ovos-stt-plugin-whisper-lm`

> ⚠️ only **python <=3.11** supported by some of the dependencies

## Models

Pretrained ngram models are provided by [HiTZ](https://huggingface.co/HiTZ/whisper-lm-ngrams)

Each lm_model is built using the KenLM toolkit and is based on n-gram statistics extracted from large, domain-specific corpora. The models available are:

- Basque (eu): `5gram-eu.bin` (11G)
- Galician (gl): `5gram-gl.bin` (8.4G)
- Catalan (ca): `5gram-ca.bin` (20G)
- Spanish (es): `5gram-es.bin` (13G)

Finetuned whisper models are also available from [Xabier Zuazo](https://huggingface.co/zuazo) for those languages

Instead of a ngram model it is also possible to use a LLM such as [latxa](https://huggingface.co/collections/HiTZ/latxa-65a697e6838b3acc53677304)

## Configuration

In the example below, we use [HiTZ Basque KenLM model](https://huggingface.co/HiTZ/whisper-lm-ngrams). Optimize the `lm_alpha`, `lm_beta`, etc., for best results with your own models.

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
> 💡 `lm_repo` only needs to be set if you want to specify a specific filename in `lm_model`


To use an LLM instead of a ngram model

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
> ⚠️ Running large LMs side-by-side with Whisper requires sufficient GPU memory.


## Credits

![](img.png)

> This plugin was funded by the Ministerio para la Transformación Digital y de la Función Pública and Plan de Recuperación, Transformación y Resiliencia - Funded by EU – NextGenerationEU within the framework of the project ILENIA with reference 2022/TL22/00215337

![](img_1.png)

The pretrained Ngram models are available under the Creative Commons Attribution 4.0 International License (CC BY 4.0). You are free to use, modify, and distribute this model as long as you credit the original creators.

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
