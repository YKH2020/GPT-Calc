# import main
# import pytest

# @pytest.mark.parametrize("image", ["VID-20231301-WA0001.mp4", "VID-20230230-WA0001.mp4"])
# def test_bad_date(image):
#     with pytest.raises(ValueError):
#         main.whatsapp_mp4(image)

# @pytest.mark.parametrize("image", ["VID20230805-WA0001.mp4", "VID-20230805-WA0001mp4"])
# def test_bad_format(image):
#     with pytest.raises(ValueError):
#         main.whatsapp_mp4(image)

# @pytest.mark.parametrize("image", ["VID--WA0001.mp4", "VID-20230805-.mp4", "-20230805-WA0001.mp4"])
# def test_missing_components(image):
#     with pytest.raises(ValueError):
#         main.whatsapp_mp4(image)

# @pytest.mark.parametrize("image", ["VID-20230805-WA#0001.mp4"])
# def test_invalid_char(image):
#     with pytest.raises(ValueError):
#         main.whatsapp_mp4(image)

# @pytest.mark.parametrize("image", ["VID-202308051-WA0001.mp4", "VID-202308-WA0001.mp4"])
# def test_invalid_length(image):
#     with pytest.raises(ValueError):
#         main.whatsapp_mp4(image)

# @pytest.mark.parametrize("image", ["VID-2023MMDD-WA0001.mp4", "VID-20230805-WA00XX.mp4"])
# def test_non_numeric(image):
#     with pytest.raises(ValueError):
#         main.whatsapp_mp4(image)

# @pytest.mark.parametrize("image", ["VID-20230805-WA0001.mp3", "VID-20230805-WA0001."])
# def test_file_extension(image):
#     with pytest.raises(ValueError):
#         main.whatsapp_mp4(image)

# """
# ======================================================= short test summary info ========================================================
# FAILED test_whatsapp_mp4.py::test_bad_format[VID-20230805-WA0001mp4] - Failed: DID NOT RAISE <class 'ValueError'>
# FAILED test_whatsapp_mp4.py::test_missing_components[VID-20230805-.mp4] - Failed: DID NOT RAISE <class 'ValueError'>
# FAILED test_whatsapp_mp4.py::test_invalid_char[VID-20230805-WA#0001.mp4] - Failed: DID NOT RAISE <class 'ValueError'>
# FAILED test_whatsapp_mp4.py::test_non_numeric[VID-20230805-WA00XX.mp4] - Failed: DID NOT RAISE <class 'ValueError'>
# FAILED test_whatsapp_mp4.py::test_file_extension[VID-20230805-WA0001.mp3] - Failed: DID NOT RAISE <class 'ValueError'>
# FAILED test_whatsapp_mp4.py::test_file_extension[VID-20230805-WA0001.] - Failed: DID NOT RAISE <class 'ValueError'>
# ===================================================== 6 failed, 8 passed in 0.06s ======================================================
# """