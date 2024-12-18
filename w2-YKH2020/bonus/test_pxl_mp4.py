# import main
# import pytest

# @pytest.mark.parametrize("image", ["PXL_20221301_123456789.mp4", "PXL_20210230_123456789.mp4"])
# def test_bad_date(image):
#     with pytest.raises(ValueError):
#         main.pxl_mp4(image)

# @pytest.mark.parametrize("image", ["PXL_20210111_250000123.mp4", "PXL_20210111_123460789.mp4", "PXL_20210111_12345699.mp4"])
# def test_bad_format(image):
#     with pytest.raises(ValueError):
#         main.pxl_mp4(image)

# @pytest.mark.parametrize("image", ["PXL__184412498.mp4", "PXL_20210111_.mp4", "_20210111_184412498.mp4"])
# def test_missing_components(image):
#     with pytest.raises(ValueError):
#         main.pxl_mp4(image)

# @pytest.mark.parametrize("image", ["PXL_20210111_18:44:12.498.mp4", "PXL_20210111_18@44@12.mp4"])
# def test_invalid_char(image):
#     with pytest.raises(ValueError):
#         main.pxl_mp4(image)

# @pytest.mark.parametrize("image", ["PXL_20210111_184412498.mp4", "PXL_20210111_18441.mp4"])
# def test_invalid_length(image):
#     with pytest.raises(ValueError):
#         main.pxl_mp4(image)

# @pytest.mark.parametrize("image", ["PXL_2021MM11_184412abc.mp4", "PXL_20210111_18ABCD123.mp4"])
# def test_non_numeric(image):
#     with pytest.raises(ValueError):
#         main.pxl_mp4(image)

# @pytest.mark.parametrize("image", ["PXL_20210111_184412498.avi", "PXL_20210111_184412498"])
# def test_file_extension(image):
#     with pytest.raises(ValueError):
#         main.pxl_mp4(image)

# """
# ======================================================= short test summary info ========================================================
# FAILED test_pxl_mp4.py::test_bad_format[PXL_20210111_250000123.mp4] - Failed: DID NOT RAISE <class 'ValueError'>
# FAILED test_pxl_mp4.py::test_bad_format[PXL_20210111_123460789.mp4] - Failed: DID NOT RAISE <class 'ValueError'>
# FAILED test_pxl_mp4.py::test_bad_format[PXL_20210111_12345699.mp4] - Failed: DID NOT RAISE <class 'ValueError'>
# FAILED test_pxl_mp4.py::test_missing_components[PXL_20210111_.mp4] - Failed: DID NOT RAISE <class 'ValueError'>
# FAILED test_pxl_mp4.py::test_missing_components[_20210111_184412498.mp4] - Failed: DID NOT RAISE <class 'ValueError'>
# FAILED test_pxl_mp4.py::test_invalid_char[PXL_20210111_18:44:12.498.mp4] - Failed: DID NOT RAISE <class 'ValueError'>
# FAILED test_pxl_mp4.py::test_invalid_char[PXL_20210111_18@44@12.mp4] - Failed: DID NOT RAISE <class 'ValueError'>
# FAILED test_pxl_mp4.py::test_invalid_length[PXL_20210111_184412498.mp4] - Failed: DID NOT RAISE <class 'ValueError'>
# FAILED test_pxl_mp4.py::test_invalid_length[PXL_20210111_18441.mp4] - Failed: DID NOT RAISE <class 'ValueError'>
# FAILED test_pxl_mp4.py::test_non_numeric[PXL_20210111_18ABCD123.mp4] - Failed: DID NOT RAISE <class 'ValueError'>
# FAILED test_pxl_mp4.py::test_file_extension[PXL_20210111_184412498.avi] - Failed: DID NOT RAISE <class 'ValueError'>
# FAILED test_pxl_mp4.py::test_file_extension[PXL_20210111_184412498] - Failed: DID NOT RAISE <class 'ValueError'>
# ===================================================== 12 failed, 4 passed in 0.07s =====================================================
# """