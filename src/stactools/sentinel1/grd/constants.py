from datetime import datetime
from typing import Any, Dict

import pystac
from pystac import Extent, ProviderRole, SpatialExtent, TemporalExtent
from pystac.extensions import sar
from pystac.extensions.eo import Band
from pystac.extensions.item_assets import AssetDefinition
from pystac.link import Link
from pystac.utils import str_to_datetime

INSPIRE_METADATA_ASSET_KEY = "inspire-metadata"
SAFE_MANIFEST_ASSET_KEY = "safe-manifest"
PRODUCT_METADATA_ASSET_KEY = "product-metadata"

SENTINEL_LICENSE = Link(
    rel="license",
    target="https://sentinel.esa.int/documents/"
    + "247904/690755/Sentinel_Data_Legal_Notice",
)

SENTINEL_PLATFORMS = ["sentinel-1a", "sentinel-1b"]

SENTINEL_GRD_DESCRIPTION = "Sentinel1 ground range detected (GRD) over CONUS. The Sentinel-1 mission is a constellation of C-band Synthetic Aperature Radar (SAR) satellites from the European Space Agency launched since 2014. These satellites collect observations of radar backscatter intensity day or night, regardless of the weather conditions, making them enormously valuable for environmental monitoring. These radar data have been processed from original Ground Range Detected (GRD) scenes into a Radiometrically Terrain Corrected, tiled product suitable for analysis. This product is available over the Contiguous United States (CONUS) since 2017 when Sentinel-1 data became globally available."  # noqa: E501

SENTINEL_GRD_START: datetime = str_to_datetime("2014-10-10T00:00:00Z")
SENTINEL_GRD_EXTENT = Extent(
    SpatialExtent([-180.0, -90.0, 180.0, 90.0]),
    TemporalExtent([[SENTINEL_GRD_START, None]]),
)

ACQUISITION_MODES = [
    "Stripmap (SM)",
    "Interferometric Wide Swath (IW)",
    "Extra Wide Swath (EW)",
    "Wave (WV)",
]
SENTINEL_CONSTELLATION = "sentinel-1"

SENTINEL_PROVIDER = pystac.Provider(
    name="ESA",
    roles=[
        ProviderRole.PRODUCER,
        ProviderRole.PROCESSOR,
        ProviderRole.LICENSOR,
    ],
    url="https://earth.esa.int/eogateway",
)

SENTINEL_GRD_PROVIDER = pystac.Provider(
    name="Sinergise",
    roles=[
        ProviderRole.HOST,
        ProviderRole.PROCESSOR,
        ProviderRole.LICENSOR,
    ],
    url="https://earth.esa.int/eogateway",
)

SENTINEL_GRD_LICENSE = Link(
    rel="license",
    target="https://scihub.copernicus.eu/twiki/do/view/SciHubWebPortal/TermsConditions",
)

SENTINEL_GRD_KEYWORDS = ["ground", "sentinel", "copernicus", "esa", "sar"]

SENTINEL_POLARIZATIONS = {
    "vh": Band.create(
        name="VH",
        description="VH band: vertical transmit and horizontal receive",
    ),
    "hh": Band.create(
        name="HH",
        description="HH band: horizontal transmit and horizontal receive",
    ),
    "hv": Band.create(
        name="HV",
        description="HV band: horizontal transmit and vertical receive",
    ),
    "vv": Band.create(
        name="VV",
        description="VV band: vertical transmit and vertical receive",
    ),
}

SENTINEL_GRD_SAR = {
    # "looks_range": [],
    "product_type": ["GRD"],
    "looks_azimuth": [1, 5],
    "polarizations": [
        sar.Polarization.HH,
        sar.Polarization.VV,
        [
            sar.Polarization.HH,
            sar.Polarization.HV,
        ],
        [
            sar.Polarization.VV,
            sar.Polarization.VH,
        ],
    ],
    "frequency_band": [sar.FrequencyBand.C],
    "instrument_mode": ["IW", "EW", "SM"],
    # "center_frequency": [],
    # "resolution_range": [],
    # "resolution_azimuth": [],
    # "pixel_spacing_range": [],
    # "observation_direction": [],
    # "pixel_spacing_azimuth": [],
    # "looks_equivalent_number": [],
}  # type: Dict[str, Any]

SENTINEL_ASSETS = {
    "VH": AssetDefinition(
        {
            "title": "VH",
            "type": "image/tiff; application=geotiff; profile=cloud-optimized",
            "description": "VH polarization backscattering coefficient, 16-bit DN.",
            "role": "data",
        }
    ),
    "HH": AssetDefinition(
        {
            "title": "HH",
            "type": "image/tiff; application=geotiff; profile=cloud-optimized",
            "description": "HH polarization backscattering coefficient, 16-bit DN.",
            "role": "data",
        }
    ),
    "HV": AssetDefinition(
        {
            "title": "HV",
            "type": "image/tiff; application=geotiff; profile=cloud-optimized",
            "description": "HV polarization backscattering coefficient, 16-bit DN.",
            "role": "data",
        }
    ),
    "VV": AssetDefinition(
        {
            "title": "VV",
            "type": "image/tiff; application=geotiff; profile=cloud-optimized",
            "description": "VV polarization backscattering coefficient, 16-bit DN.",
            "role": "data",
        }
    ),
}
