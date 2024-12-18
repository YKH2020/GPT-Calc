# import main
# import pytest

# @pytest.mark.parametrize("image", ["IMG-20231301-WA0004.jpg", "IMG-20210230-WA0004.jpg"])
# def test_bad_date(image):
#     with pytest.raises(ValueError):
#         main.whatsapp_image(image)

# @pytest.mark.parametrize("image", ["IMG-20190408-WA250000.jpg", "IMG-20190408-WA12345678.jpg", "IMG-20190408-WA12345.jpg"])
# def test_bad_format(image):
#     with pytest.raises(ValueError):
#         main.whatsapp_image(image)

# @pytest.mark.parametrize("image", ["IMG--WA0004.jpg", "IMG-20190408-.jpg", "-20190408-WA0004.jpg"])
# def test_missing_components(image):
#     with pytest.raises(ValueError):
#         main.whatsapp_image(image)

# @pytest.mark.parametrize("image", ["IMG-20190408-WA#004.jpg", "IMG-20190408-WA0004!jpg"])
# def test_invalid_char(image):
#     with pytest.raises(ValueError):
#         main.whatsapp_image(image)

# @pytest.mark.parametrize("image", ["IMG-20190408-WA0004.jpg", "IMG-20190408-WA000.jpg"])
# def test_invalid_length(image):
#     with pytest.raises(ValueError):
#         main.whatsapp_image(image)

# @pytest.mark.parametrize("image", ["IMG-2019MM08-WA0004.jpg", "IMG-20190408-WA00XX.jpg"])
# def test_non_numeric(image):
#     with pytest.raises(ValueError):
#         main.whatsapp_image(image)

# @pytest.mark.parametrize("image", ["IMG-20190408-WA0004.png", "IMG-20190408-WA0004"])
# def test_file_extension(image):
#     with pytest.raises(ValueError):
#         main.whatsapp_image(image)

# """
# ======================================================= short test summary info ========================================================
# FAILED test_whatsapp_image.py::test_bad_format[IMG-20190408-WA250000.jpg] - Failed: DID NOT RAISE <class 'ValueError'>
# FAILED test_whatsapp_image.py::test_bad_format[IMG-20190408-WA12345678.jpg] - Failed: DID NOT RAISE <class 'ValueError'>
# FAILED test_whatsapp_image.py::test_bad_format[IMG-20190408-WA12345.jpg] - Failed: DID NOT RAISE <class 'ValueError'>
# FAILED test_whatsapp_image.py::test_missing_components[IMG-20190408-.jpg] - Failed: DID NOT RAISE <class 'ValueError'>
# FAILED test_whatsapp_image.py::test_invalid_char[IMG-20190408-WA#004.jpg] - Failed: DID NOT RAISE <class 'ValueError'>
# FAILED test_whatsapp_image.py::test_invalid_char[IMG-20190408-WA0004!jpg] - Failed: DID NOT RAISE <class 'ValueError'>
# FAILED test_whatsapp_image.py::test_invalid_length[IMG-20190408-WA0004.jpg] - Failed: DID NOT RAISE <class 'ValueError'>
# FAILED test_whatsapp_image.py::test_invalid_length[IMG-20190408-WA000.jpg] - Failed: DID NOT RAISE <class 'ValueError'>
# FAILED test_whatsapp_image.py::test_non_numeric[IMG-20190408-WA00XX.jpg] - Failed: DID NOT RAISE <class 'ValueError'>
# FAILED test_whatsapp_image.py::test_file_extension[IMG-20190408-WA0004.png] - Failed: DID NOT RAISE <class 'ValueError'>
# FAILED test_whatsapp_image.py::test_file_extension[IMG-20190408-WA0004] - Failed: DID NOT RAISE <class 'ValueError'>
# ===================================================== 11 failed, 5 passed in 0.07s =====================================================
# """