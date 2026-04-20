from dataclass import dataclass
from burst import BurstGenerator, WhiteNoise

AUDIO_CD_SAMPLING_RATE = 44100

@dataclass(frozen=True)
class Synthesizer:
    