# import main
# import pytest

# # Edge cases for MP4 files
# @pytest.mark.parametrize("image", ["VID-20231301-WA0001.mp4", "VID-20210230-WA0001.mp4"])
# def test_bad_date_mp4(image):
#     with pytest.raises(ValueError):
#         main.detect_mp4(image)

# @pytest.mark.parametrize("image", ["VID-20210111-WA250000.mp4", "VID-20210111-WA12345678.mp4", "VID-20210111-WA12345.mp4"])
# def test_bad_format_mp4(image):
#     with pytest.raises(ValueError):
#         main.detect_mp4(image)

# @pytest.mark.parametrize("image", ["VID--WA0001.mp4", "VID-20210111-.mp4", "-20210111-WA0001.mp4"])
# def test_missing_components_mp4(image):
#     with pytest.raises(ValueError):
#         main.detect_mp4(image)

# @pytest.mark.parametrize("image", ["VID-20210111-WA#001.mp4", "VID-20210111-WA0001!mp4"])
# def test_invalid_char_mp4(image):
#     with pytest.raises(ValueError):
#         main.detect_mp4(image)

# @pytest.mark.parametrize("image", ["VID-20210111-WA0001.mp4", "VID-20210111-WA000.mp4"])
# def test_invalid_length_mp4(image):
#     with pytest.raises(ValueError):
#         main.detect_mp4(image)

# @pytest.mark.parametrize("image", ["VID-2019MMDD-WA0001.mp4", "VID-20210111-WA00XX.mp4"])
# def test_non_numeric_mp4(image):
#     with pytest.raises(ValueError):
#         main.detect_mp4(image)

# @pytest.mark.parametrize("image", ["VID-20210111-WA0001.avi", "VID-20210111-WA0001"])
# def test_file_extension_mp4(image):
#     with pytest.raises(ValueError):
#         main.detect_mp4(image)

# # Edge cases for WhatsApp files
# @pytest.mark.parametrize("image", ["IMG-20231301-WA0004.jpg", "IMG-20210230-WA0004.jpg"])
# def test_bad_date_whatsapp(image):
#     with pytest.raises(ValueError):
#         main.detect_whatsapp_file(image)

# @pytest.mark.parametrize("image", ["IMG-20210111-WA250000.jpg", "IMG-20210111-WA12345678.jpg", "IMG-20210111-WA12345.jpg"])
# def test_bad_format_whatsapp(image):
#     with pytest.raises(ValueError):
#         main.detect_whatsapp_file(image)

# @pytest.mark.parametrize("image", ["IMG--WA0004.jpg", "IMG-20210111-.jpg", "-20210111-WA0004.jpg"])
# def test_missing_components_whatsapp(image):
#     with pytest.raises(ValueError):
#         main.detect_whatsapp_file(image)

# @pytest.mark.parametrize("image", ["IMG-20210111-WA#004.jpg", "IMG-20210111-WA0004!jpg"])
# def test_invalid_char_whatsapp(image):
#     with pytest.raises(ValueError):
#         main.detect_whatsapp_file(image)

# @pytest.mark.parametrize("image", ["IMG-20210111-WA0004.jpg", "IMG-20210111-WA000.jpg"])
# def test_invalid_length_whatsapp(image):
#     with pytest.raises(ValueError):
#         main.detect_whatsapp_file(image)

# @pytest.mark.parametrize("image", ["IMG-2019MM08-WA0004.jpg", "IMG-20210111-WA00XX.jpg"])
# def test_non_numeric_whatsapp(image):
#     with pytest.raises(ValueError):
#         main.detect_whatsapp_file(image)

# @pytest.mark.parametrize("image", ["IMG-20210111-WA0004.png", "IMG-20210111-WA0004"])
# def test_file_extension_whatsapp(image):
#     with pytest.raises(ValueError):
#         main.detect_whatsapp_file(image)

# """
# ========================================================= short test summary info =========================================================
# FAILED test_detections.py::test_bad_format_mp4[VID-20210111-WA250000.mp4] - Failed: DID NOT RAISE <class 'ValueError'>
# FAILED test_detections.py::test_bad_format_mp4[VID-20210111-WA12345678.mp4] - Failed: DID NOT RAISE <class 'ValueError'>
# FAILED test_detections.py::test_bad_format_mp4[VID-20210111-WA12345.mp4] - Failed: DID NOT RAISE <class 'ValueError'>
# FAILED test_detections.py::test_missing_components_mp4[VID-20210111-.mp4] - Failed: DID NOT RAISE <class 'ValueError'>
# FAILED test_detections.py::test_missing_components_mp4[-20210111-WA0001.mp4] - Failed: DID NOT RAISE <class 'ValueError'>
# FAILED test_detections.py::test_invalid_char_mp4[VID-20210111-WA#001.mp4] - Failed: DID NOT RAISE <class 'ValueError'>
# FAILED test_detections.py::test_invalid_char_mp4[VID-20210111-WA0001!mp4] - Failed: DID NOT RAISE <class 'ValueError'>
# FAILED test_detections.py::test_invalid_length_mp4[VID-20210111-WA0001.mp4] - Failed: DID NOT RAISE <class 'ValueError'>
# FAILED test_detections.py::test_invalid_length_mp4[VID-20210111-WA000.mp4] - Failed: DID NOT RAISE <class 'ValueError'>
# FAILED test_detections.py::test_non_numeric_mp4[VID-20210111-WA00XX.mp4] - Failed: DID NOT RAISE <class 'ValueError'>
# FAILED test_detections.py::test_file_extension_mp4[VID-20210111-WA0001.avi] - Failed: DID NOT RAISE <class 'ValueError'>
# FAILED test_detections.py::test_file_extension_mp4[VID-20210111-WA0001] - Failed: DID NOT RAISE <class 'ValueError'>
# FAILED test_detections.py::test_bad_format_whatsapp[IMG-20210111-WA250000.jpg] - Failed: DID NOT RAISE <class 'ValueError'>
# FAILED test_detections.py::test_bad_format_whatsapp[IMG-20210111-WA12345678.jpg] - Failed: DID NOT RAISE <class 'ValueError'>
# FAILED test_detections.py::test_bad_format_whatsapp[IMG-20210111-WA12345.jpg] - Failed: DID NOT RAISE <class 'ValueError'>
# FAILED test_detections.py::test_missing_components_whatsapp[IMG-20210111-.jpg] - Failed: DID NOT RAISE <class 'ValueError'>
# FAILED test_detections.py::test_missing_components_whatsapp[-20210111-WA0004.jpg] - Failed: DID NOT RAISE <class 'ValueError'>
# FAILED test_detections.py::test_invalid_char_whatsapp[IMG-20210111-WA#004.jpg] - Failed: DID NOT RAISE <class 'ValueError'>
# FAILED test_detections.py::test_invalid_char_whatsapp[IMG-20210111-WA0004!jpg] - Failed: DID NOT RAISE <class 'ValueError'>
# FAILED test_detections.py::test_invalid_length_whatsapp[IMG-20210111-WA0004.jpg] - Failed: DID NOT RAISE <class 'ValueError'>
# FAILED test_detections.py::test_invalid_length_whatsapp[IMG-20210111-WA000.jpg] - Failed: DID NOT RAISE <class 'ValueError'>
# FAILED test_detections.py::test_non_numeric_whatsapp[IMG-20210111-WA00XX.jpg] - Failed: DID NOT RAISE <class 'ValueError'>
# FAILED test_detections.py::test_file_extension_whatsapp[IMG-20210111-WA0004.png] - Failed: DID NOT RAISE <class 'ValueError'>
# FAILED test_detections.py::test_file_extension_whatsapp[IMG-20210111-WA0004] - Failed: DID NOT RAISE <class 'ValueError'>
# ====================================================== 24 failed, 8 passed in 0.13s =======================================================
# """