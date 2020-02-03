from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import json

driver = webdriver.Chrome()
driver.get('http://www.portaltransparencia.gov.br/')

# Acessa pagina dos servidores
driver.find_element_by_id('servidores-card').click()
aTagsInLi = driver.find_elements_by_css_selector('li a')
for a in aTagsInLi:
    if a.get_attribute('href') == 'http://www.portaltransparencia.gov.br/servidores/lista-consultas':
        a.click()
        break

# Seleciona consulta por vinculo 
driver.find_element_by_xpath('/html/body/main/div[2]/div/div/ul/li[2]/a').click()

#Seleciona os servidores do tipo militar e civil
driver.find_element_by_xpath('//*[@id="id-box-filtro"]/div/div/ul/li[10]/div/button').click()

try:
    militar = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="id-box-filtro"]/div/div/ul/li[10]/div/div/div/div[2]/div[2]/ul/li[3]/a/label/input'))
    )
    civil = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="id-box-filtro"]/div/div/ul/li[10]/div/div/div/div[2]/div[2]/ul/li[4]/a/label/input'))
    )
    
finally:
    driver.find_element_by_xpath('//*[@id="id-box-filtro"]/div/div/ul/li[10]/div/div/div/div[2]/div[2]/ul/li[3]/a/label/input').click()
    driver.find_element_by_xpath('//*[@id="id-box-filtro"]/div/div/ul/li[10]/div/div/div/div[2]/div[2]/ul/li[4]/a/label/input').click()
    driver.find_element_by_xpath('//*[@id="id-box-filtro"]/div/div/ul/li[10]/div/div/div/div[2]/div[2]/ul/li[2]/input').click()

driver.find_element_by_class_name('botao__gera_paginacao_completa').click()


## Retirando dados de cada servidor
aTagsInTd = driver.find_elements_by_css_selector('td a')


pagina_servidores = []
for a in aTagsInTd:
    pagina_servidores.append(a.get_attribute('href'))
    
    
for pagina in pagina_servidores:
    print(pagina)
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(pagina)
    
    nome = driver.find_element_by_xpath("/html/body/main/div[2]/section[1]/div[1]/div[1]/span").text
    print(nome)
    cpf = driver.find_element_by_xpath("/html/body/main/div[2]/section[1]/div[1]/div[2]/span/a").text
    print(cpf)
    servidor = driver.find_element_by_xpath("/html/body/main/div[2]/section[1]/div[1]/div[3]/span").text
    print(servidor)
    licença = driver.find_element_by_xpath("/html/body/main/div[2]/section[1]/div[2]/div[1]/span").text
    print(licença)
    uf = driver.find_element_by_xpath("/html/body/main/div[2]/section[1]/div[2]/div[2]/span").text
    print(uf)
    local_de_trabalho = driver.find_element_by_xpath("/html/body/main/div[2]/section[1]/div[3]/div[1]/span").text
    print(local_de_trabalho)
    ingresso_no_serviço_publico = driver.find_element_by_xpath("/html/body/main/div[2]/section[1]/div[3]/div[2]/span").text
    print(ingresso_no_serviço_publico)

    ## retira dados da ficha de remuneraçao
    driver.find_element_by_id('botao-box-remuneracao').click()


    try:
        remuneracao_eventual_grat_natalina = driver.find_element_by_xpath('//*[@id="tab-remuneracoes-1"]/div/div[4]/div[2]/span[1]').text
        print(remuneracao_eventual_grat_natalina)

    except NoSuchElementException:
        remuneracao_eventual_grat_natalina = None
        print('nao tem eventual grat natalina')
    
    try:
        remuneracao_eventual_ferias = driver.find_element_by_xpath('//*[@id="tab-remuneracoes-1"]/div/div[4]/div[2]/span[2]').text
        print(remuneracao_eventual_ferias)

    except NoSuchElementException:
        remuneracao_eventual_ferias = None
        print('nao tem eventual ferias')
    
    try:
        remuneracao_eventual_outras = driver.find_element_by_xpath('//*[@id="tab-remuneracoes-1"]/div/div[4]/div[2]/span[3]').text
        print(remuneracao_eventual_outras)

    except NoSuchElementException:
        remuneracao_eventual_outras = None
        print('nao tem eventual outras')
    
    try:
        deduçoes_obrigatorias_irrf = driver.find_element_by_xpath('//*[@id="tab-remuneracoes-1"]/div/div[5]/div[3]/span[1]').text
        print(deduçoes_obrigatorias_irrf)

    except NoSuchElementException:
        deduçoes_obrigatorias_irrf = None
        print('nao tem irrf')
    
    try:
        deduçoes_obrigatorias_pss_rpgs = driver.find_element_by_xpath('//*[@id="tab-remuneracoes-1"]/div/div[5]/div[3]/span[2]').text
        print(deduçoes_obrigatorias_pss_rpgs)

    except NoSuchElementException:
        deduçoes_obrigatorias_pss_rpgs = None
        print('nao tem pss rpgs')
    
    try: 
        deduçoes_obrigatorias_pensao_militar = driver.find_element_by_xpath('//*[@id="tab-remuneracoes-1"]/div/div[5]/div[3]/span[3]').text
        print(deduçoes_obrigatorias_pensao_militar)

    except NoSuchElementException:
        deduçoes_obrigatorias_pensao_militar = None
        print('nao tem pensao militar')
    
    try:
        deduçoes_obrigatorias_fundo_saude = driver.find_element_by_xpath('//*[@id="tab-remuneracoes-1"]/div/div[5]/div[3]/span[4]').text
        print(deduçoes_obrigatorias_fundo_saude)

    except NoSuchElementException:
        deduçoes_obrigatorias_fundo_saude = None
        print('nao tem fundo saude')
    
    try: 
        total_remuneracao = driver.find_element_by_xpath('//*[@id="tab-remuneracoes-1"]/div/div[6]/div[2]/strong').text
        print(total_remuneracao)

    except NoSuchElementException:
        total_remuneracao = None
        print('nao tem total remuneracao')
    
    try:
        remuneracao_basica = driver.find_element_by_xpath('//*[@id="tab-remuneracoes-1"]/div/div[2]/div[2]/span').text
        print(remuneracao_basica)

    except NoSuchElementException:
        remuneracao_basica = None
        print('nao tem remuneracao basica')
    
    ## retira dados do historico
    driver.find_element_by_id('botao-historico-poder-executivo').click()

    tabela = driver.find_element_by_id('tabela-historico-poder-executivo')

    linhas = tabela.find_element_by_tag_name('tbody').find_elements_by_tag_name('tr')

    historico_dos_vinculos = []

    for linha in range(len(linhas)):
        tdInTr = linhas[linha].find_element_by_tag_name('td')
        key_list = ['TIPO DE VINCULO', 'DATA DE INICIO DE VINCULO', 'DATA DE TERMINIO DO VINCULO',
            'ORGAO/ENTIDADE', 'CARGO/EMPREGO/FUNCAO COMISSADA'] 
        dic = {}

        for i in key_list:
            dic[i] = None
    
        for td in range(1,6): 
    
            dic[key_list[td-1]] = driver.find_element_by_xpath('//*[@id="tabela-historico-poder-executivo"]/tbody/tr['+str(linha+1)+']/td['+str(td)+']').text
    
        historico_dos_vinculos.append(json.dumps(dic))
        
    print(historico_dos_vinculos)
    
    driver.close()

    driver.switch_to.window(driver.window_handles[0])
   