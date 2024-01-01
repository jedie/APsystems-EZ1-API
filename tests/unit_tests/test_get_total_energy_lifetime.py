import pytest


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "output_data, expected_total_energy, test_id",
    [
        # Happy path tests with various realistic test values
        (
            {
                "data": {
                    "te1": 5000.0,
                    "te2": 3000.0,
                    "e1": 0.0,
                    "e2": 0.0,
                    "p1": 0.0,
                    "p2": 0.0,
                }, "status": 0
            },
            8000.0,
            "happy_path_1",
        ),
        (
            {
                "data": {
                    "te1": 1234.56,
                    "te2": 789.01,
                    "e1": 0.0,
                    "e2": 0.0,
                    "p1": 0.0,
                    "p2": 0.0,
                }, "status": 0
            },
            2023.57,
            "happy_path_2",
        ),
        # Edge cases
        (
            {
                "data": {
                    "te1": 0.0,
                    "te2": 3000.0,
                    "e1": 0.0,
                    "e2": 0.0,
                    "p1": 0.0,
                    "p2": 0.0,
                }, "status": 0
            },
            3000.0,
            "edge_case_1",
        ),
        (
            {
                "data": {
                    "te1": 3000.0,
                    "te2": 0.0,
                    "e1": 0.0,
                    "e2": 0.0,
                    "p1": 0.0,
                    "p2": 0.0,
                }, "status": 0
            },
            3000.0,
            "edge_case_2",
        ),
        ## Error cases
        (None, None, "error_case_1"),
    ],
)
async def test_get_total_energy_lifetime(
    output_data, expected_total_energy, test_id, mock_response
):
    # Arrange
    ez1m = mock_response(output_data)

    # Act
    total_energy = await ez1m.get_total_energy_lifetime()

    # Assert
    assert total_energy == expected_total_energy, f"Test failed for {test_id}"
