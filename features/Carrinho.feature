Feature: Carrinho de Compra Pet
  Scenario: Compra de produto
    Given que acesso o site Petz
    And Clico no botao aceito politica de privacidade
    Then clico no texbox de pesquisa
    And limpo o campo
    And digito o nome do produto "Biscoito Golden Cookie para Cães Adultos 350g"
    Then clico no enter
    When clico no botao adcionar ao carrinho
    Then valido se o produto confere
    And valido se o preco e igual ao informado na pagina de pesquisa

