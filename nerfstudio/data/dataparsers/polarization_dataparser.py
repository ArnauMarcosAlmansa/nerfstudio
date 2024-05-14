from dataclasses import dataclass, field
from pathlib import Path
from pprint import PrettyPrinter
from typing import Type, Optional, Literal

from nerfstudio.utils.io import load_from_json

from nerfstudio.data.dataparsers.base_dataparser import DataParserConfig, DataparserOutputs


@dataclass
class PolarizationDataParserConfig(DataParserConfig):
    """Nerfstudio dataset config"""

    _target: Type = field(default_factory=lambda: PolarizationDataParser)
    """target class to instantiate"""
    data: Path = Path("data/nerfstudio/poster")
    """Directory specifying location of data."""
    scale_factor: float = 1.0
    """How much to scale the camera origins by."""
    downscale_factor: Optional[int] = None
    """How much to downscale images. If not set, images are chosen such that the max dimension is <1600px."""
    scene_scale: float = 1.0
    """How much to scale the region of interest by."""
    orientation_method: Literal["pca", "up", "vertical", "none"] = "up"
    """The method to use for orientation."""
    center_method: Literal["poses", "focus", "none"] = "poses"
    """The method to use to center the poses."""
    auto_scale_poses: bool = True
    """Whether to automatically scale the poses to fit in +/- 1 bounding box."""
    train_split_fraction: float = 0.9
    """The fraction of images to use for training. The remaining images are for eval."""
    depth_unit_scale_factor: float = 1e-3
    """Scales the depth values to meters. Default value is 0.001 for a millimeter to meter conversion."""



@dataclass
class PolarizationDataParser:
    config: PolarizationDataParserConfig

    def _generate_dataparser_outputs(self, split="train"):
        meta = load_from_json(self.config.data / "transforms.json")


        pp = PrettyPrinter()
        pp.pprint(meta)

        image_filenames = []
        poses = []
        ...
        dataparser_outputs = DataparserOutputs(
            image_filenames=image_filenames,
            cameras=cameras,
            scene_box=scene_box,
        )
        return dataparser_outputs

