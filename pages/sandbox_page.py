from selenium.webdriver.common.by import By
from .base_page import BasePage


class SandboxPage(BasePage):
    ENVIAR_BUTTON = (By.XPATH, "//button[contains(text(), 'Enviar')]")
    DYNAMIC_ID_BUTTON = (
        By.XPATH,
        "//button[contains(text(), 'Hacé click para generar un ID dinámico y mostrar el elemento oculto')]",
    )
    HIDDEN_TEXT_LABEL = (
        By.XPATH,
        "//p[contains(text(), 'OMG, aparezco después de 3 segundos de haber hecho click en el botón')]",
    )

    def navigate_sandbox(self):
        self.navigate_to(
            "https://thefreerangetester.github.io/sandbox-automation-testing/"
        )

    def click_enviar(self):
        self.click(self.ENVIAR_BUTTON)

    def click_boton_id_dinamico(self):
        self.click(self.DYNAMIC_ID_BUTTON)

    def hover_over_dynamic_id_button(self):
        self.hover_over_element(self.DYNAMIC_ID_BUTTON)

    def select_checkbox_with_label(self, label_text):
        checkbox_locator = (
            By.XPATH,
            f"//label[contains(., '{label_text}')]/preceding-sibling::input[@type='checkbox']",
        )
        self.select_element(checkbox_locator)
