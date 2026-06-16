"""Lightweight interface tests for WhisperLMSTT.

These never instantiate the plugin (instantiation downloads Whisper and KenLM
models from Hugging Face), they only assert the class shape and contract.
"""
import inspect

from ovos_plugin_manager.templates.stt import STT

from ovos_stt_plugin_whisper_lm import WhisperLMSTT


def test_subclasses_stt_template():
    assert issubclass(WhisperLMSTT, STT)


def test_exposes_expected_methods():
    assert hasattr(WhisperLMSTT, "execute")
    assert callable(WhisperLMSTT.execute)
    # execute(self, audio, language=None)
    params = list(inspect.signature(WhisperLMSTT.execute).parameters)
    assert params[:2] == ["self", "audio"]
    assert "language" in params


def test_available_languages():
    langs = WhisperLMSTT.available_languages
    assert isinstance(langs, set)
    assert langs == {"gl", "es", "eu", "ca"}


def test_entrypoint_registered():
    from ovos_plugin_manager.stt import find_stt_plugins

    plugins = find_stt_plugins()
    assert "ovos-stt-plugin-whisper-lm" in plugins
    assert plugins["ovos-stt-plugin-whisper-lm"] is WhisperLMSTT
