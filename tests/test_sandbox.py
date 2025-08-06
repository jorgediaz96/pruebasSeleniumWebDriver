import pytest

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_boton_id_dinamico_muestra_texto_al_hacer_click(sandbox_page):
    sandbox_page.navigate_sandbox()
    sandbox_page.click_boton_id_dinamico()

    # Estamos usando el wait_for_element para esperar que el elemento sea visible
    elemento_texto_oculto = sandbox_page.wait_for_element(
        sandbox_page.HIDDEN_TEXT_LABEL
    )

    # Creamos la variable con el texto esperado y hacemos el assertion
    texto_esperado = (
        "OMG, aparezco después de 3 segundos de haber hecho click en el botón"
    )

    assert (
        texto_esperado in elemento_texto_oculto.text
    ), "El texto esperado no coincide con el texto encontrado"


def test_boton_id_dinamico_cambiar_color_al_hacer_hover(sandbox_page):
    sandbox_page.navigate_sandbox()

    boton_id_dinamico = sandbox_page.wait_for_element(sandbox_page.DYNAMIC_ID_BUTTON)

    # Obtenemos el color del botón ANTES de hacer hover
    color_before_hover = boton_id_dinamico.value_of_css_property("background-color")

    # Usamos el método hover_over_element de BasePage para simular el hover
    sandbox_page.hover_over_dynamic_id_button()

    # Obtener el color después del Hover
    color_after_hover = boton_id_dinamico.value_of_css_property("background-color")

    # Validar con un assertion que efectivamente son distintos valores antes y después del hover
    assert color_before_hover != color_after_hover


@pytest.mark.sandbox
@pytest.mark.regresion
def test_elegir_checkbox(sandbox_page):
    sandbox_page.navigate_sandbox()
    sandbox_page.select_checkbox_with_label("Pizza")
