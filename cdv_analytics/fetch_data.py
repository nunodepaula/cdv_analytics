"""Fetch data from SIGEL/ANEEL.

@Author: Nuno de Paula
@date: 28-11-2024
"""

import json
from http import HTTPStatus
from pathlib import Path

import requests


def fetch_data(start_id: int = 0, end_id: int = 24000, step: int = 1000) -> None:
    """Fetch wind turbines data from SIGEL/ANEEL.

    This functions performs multiple requests to SIGEL to fetch the data with id between start_id and end_id.

    Args:
        start_id (int, optional): First id of the fetched data. Defaults to 0.
        end_id (int, optional): Last id for the fetched data. Defaults to 24000.
        step (int, optional): Maximum number of ids per request. Defaults to 1000.

    Raises:
        ValueError: If the request fail or return an error code.
    """
    data_path = Path(__file__).parent.parent / "outputs" / "sigel"
    data_path.mkdir(parents=True, exist_ok=True)

    for i in range(start_id, end_id, step):
        response = requests.get(
            f"https://sigel.aneel.gov.br/arcgis/rest/services/PORTAL/WFS/MapServer/0/query?where=OBJECTID>{i}&timeRelation=esriTimeRelationOverlaps&geometryType=esriGeometryEnvelope&spatialRel=esriSpatialRelIntersects&units=esriSRUnit_Meter&outFields=*&returnGeometry=true&returnTrueCurves=false&returnIdsOnly=false&returnCountOnly=false&returnZ=false&returnM=false&returnDistinctValues=false&returnExtentOnly=false&sqlFormat=none&featureEncoding=esriDefault&f=geojson",
            timeout=10,
        )
        if response.status_code != HTTPStatus.OK:
            msg = "Failed to fetch data."
            raise ValueError(msg)

        with (data_path / f"aerogeradores_{i+1}-{i+step}.geojson").open("w") as file:
            json.dump(response.json(), file)
