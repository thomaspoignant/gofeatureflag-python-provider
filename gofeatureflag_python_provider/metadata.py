from dataclasses import dataclass

from open_feature.provider.metadata import Metadata


@dataclass
class GoFeatureFlagMetadata(Metadata):
    name: str = "GO Feature Flag"
