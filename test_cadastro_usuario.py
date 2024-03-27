# Generated by Selenium IDE
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from faker import Faker
class TestCadastroUsuario():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_cadastrousurioGF(self):
    fake = Faker('pt_br')
    email = fake.email()
    cpf = fake.cpf()

    self.driver.get("https://www.giulianaflores.com.br/")
    self.driver.set_window_size(1382, 744)
    self.driver.find_element(By.ID, "perfil-hidden").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    self.driver.find_element(By.CSS_SELECTOR, "#UrlLogin > a").click()
    self.driver.find_element(By.ID, "ContentSite_ibtNewCustomer").click()
    self.driver.find_element(By.ID, "ContentSite_txtName").click()
    self.driver.find_element(By.ID, "ContentSite_txtName").send_keys("Teste Iterasys")
    self.driver.find_element(By.ID, "ContentSite_txtCpf").click()
    self.driver.find_element(By.ID, "ContentSite_txtCpf").send_keys(cpf)
    self.driver.find_element(By.ID, "ContentSite_txtEmail").click()
    self.driver.find_element(By.ID, "ContentSite_txtEmail").send_keys(email)
    self.driver.find_element(By.ID, "ContentSite_txtPasswordNew").click()
    self.driver.find_element(By.ID, "ContentSite_txtPasswordNew").send_keys("manuela@123")
    self.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtZip").click()
    self.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtZip").click()
    self.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtZip").send_keys("14783-114")
    # Utilizando o time sleep pois os dados de endereco estao carregando muito rápido 
    time.sleep(2)
    self.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtAddressNumber").click()
    self.driver.execute_script("window.scrollTo(0,701)")
    self.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtAddressNumber").send_keys("541")
    self.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtPhoneCelularNum").click()
    self.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtPhoneCelularNum").send_keys("17986826945")
    self.driver.find_element(By.CSS_SELECTOR, ".col:nth-child(2)").click()
    self.driver.find_element(By.ID, "ContentSite_btnCreateCustomer").click()