import os #importamos a bilbioteca os
import pyttsx3 #importamos a bliblioteca pyttsx3
import speech_recognition as sr #imporatmos a biblioteca speech_recognition
import winsound

BUFFER_SIZE = 1024 #tempo até que o audio seja executado.
chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe' #caminho do chrome

r = sr.Recognizer() #instancia o reconhecedor

with sr.Microphone() as source: #inicia a função de reconhecimento (speech recognition)
        r.adjust_for_ambient_noise(source) #bloqueia barulhos de ambiente
        engine = pyttsx3.init() #insere a biblioteca no engine
        engine.say('Bem vindo a Cognizant ') #frase de boas vindas
        engine.runAndWait() #espera o fim da fala
        
#### menu ####
print("opções:") 
print("\nFALE SOBRE - para saber sobre nós.")
print("\nFALE SOMA - para efetuar a soma de dois números.")
print("\nFALE HISTÓRIA - para saber sobre nossa crescimento.")
print("\nFALE NEGOCIOS - para saber sobre nossa metodologia de trabalho.")
print("\nFALE DIGITAL - para saber sobre digital business.")
print("\nFALE CONTATO - para falar conosco.")
print("\nFALE SETOR - areas do digital business.")
print("\nFALE GOOGLE - para abrir o navegador Chrome.")
print("\nFALE MÚSICA - e depois fale 'PLAY' Para ouvir uma musica.")
print("\nFALE FECHAR - para finalizar o programa.")
print("\nO que você gostaria de saber sobre a Cognizant hoje?")


##### Definições #####
def  abrirGoogle():      
    print("Abrindo Google...") 
    os.startfile(chrome_path)
              
def soma(): #função para executar soma
    engine = pyttsx3.init()
   

    try:
          x = int(input("número1: ")) #recebe o numero 1 , tem que digitar
          y = int(input("número2: ")) #recebe numero 2  
          soma = x+y#faz a soma
          intro=engine.say(' O resultado da soma de {} + {} = {}'.format(x,y,soma))
          engine.runAndWait()
          print("{} + {} = {}".format(x,y,soma))
    
    
    except ValueError:
             print ('Insira somente números')
             
            
   
    
    #escreve

def sair(): #função sair
    engine = pyttsx3.init()
    intro=engine.say('Até logo')
    engine.runAndWait()
    fechar=intro
    
def sobre(): #função sobre
    engine = pyttsx3.init()
    intro=engine.say('Somos líderes globais em serviços voltados para os negócios e a tecnologia, ajudando os nossos clientes, hoje, a dar vida ao futuro do trabalho. ')
    engine.runAndWait()
    intro=("Somos líderes globais em serviços voltados para os negócios e a tecnologia, ajudando os nossos clientes, hoje, a dar vida ao futuro do trabalho.")
    sobre=intro
    print(sobre)
                        
def história(): #função historia
    engine = pyttsx3.init()
    crescimento=engine.say("nós somos duros no trabalho que prevê e que constrói a economia digital. Fazemos isso para apoiar nossos clientes, muitos dos quais servem como pilares da economia global. Com conhecimento como seu parceiro, eles estão combinando seus ativos e conhecimentos com poderosas tecnologias digitais para gerar novos fluxos de receita, novos modelos operacionais, e totalmente novas formas de deliciar seus clientes. Como resultado, esses clientes estão emergindo como uma nova geração de pesos pesados digitais. E estamos investindo agressivamente para construir continuamente novas capacidades para ajudá-los a ganhar com digital.")
    engine.runAndWait()
    crescimento=("nós somos duros no trabalho que prevê e que constrói a economia digital. Fazemos isso para apoiar nossos clientes, muitos dos quais servem como pilares da economia global. Com conhecimento como seu parceiro, eles estão combinando seus ativos e conhecimentos com poderosas tecnologias digitais para gerar novos fluxos de receita, novos modelos operacionais, e totalmente novas formas de deliciar seus clientes. Como resultado, esses clientes estão emergindo como uma nova geração de pesos pesados digitais. E estamos investindo agressivamente para construir continuamente novas capacidades para ajudá-los a ganhar com digital.")
    historia=crescimento
    print(historia)

def negocios(): #função negocios
    engine = pyttsx3.init()
    trabalho=engine.say("Alinhado com as necessidades dos nossos clientes-Ser digital em escala requer que as organizações executem de uma perspectiva holística em seus modelos de negócios, operacionais e tecnológicos. Veja como as nossas três áreas de prática permitem isso para clientes, em todo o mundo.")
    engine.runAndWait()
    trabalho=("Alinhado com as necessidades dos nossos clientes-Ser digital em escala requer que as organizações executem de uma perspectiva holística em seus modelos de negócios, operacionais e tecnológicos. Veja como as nossas três áreas de prática permitem isso para clientes, em todo o mundo.")
    negocios=trabalho
    print(negocios)
                       
def digital(): #função digital
    engine = pyttsx3.init()
    business=engine.say(" Ajudamos você a reinventar produtos, experiências e modelos de negócios para criar novo valor, diferenciação e receita na economia digital")
    engine.runAndWait()
    business=("Ajudamos você a reinventar produtos, experiências e modelos de negócios para criar novo valor, diferenciação e receita na economia digital")
    digital= business
    print(digital)
                        
def contato(): #função contato
    engine = pyttsx3.init()
    conversa=engine.say("https://www.cognizant.com/pt-br/")
    engine.runAndWait()
    conversa=("https://www.cognizant.com/pt-br/")
    contato= conversa
    print(contato)

def setor(): #função setor
    engine = pyttsx3.init()
    areas=engine.say("ciencia, manufaturas, servicos financeiros e bancarios,turismo, hospitalar,energia,comunicacoes, saude, seguranca da informacao")
    engine.runAndWait()
    areas=("ciencia, manufaturas, servicos financeiros e bancarios,turismo, hospitalar,energia,comunicacoes, saude, seguranca da informacao")
    setor= areas
    print(setor)
    
def verificaMusica():  #vai tocar a musica
    # abrindo o arquivo como binario
    print("Carregando música...")
    winsound.PlaySound('oi.wav', winsound.SND_FILENAME)
        
    
####

                        
with sr.Microphone() as source:  #chamando a gravação do microfone
    while True:
                r.adjust_for_ambient_noise(source) #bloqueia ruidos do ambiente
                print("Diga algo!") 
                audio = r.listen(source,phrase_time_limit=10) #capta o que foi dito
                try: 
                        print("Você disse: "+  r.recognize_google(audio, language="pt-BR")) #sintetiza a voz e trasncreve em texto
                except sr.UnknownValueError:  #caso de valor incompreensivel:
                        print("Não pude enteder o audio")
                        continue
                except sr.ResquestError as e:
                        print("Erro ao chamar Google Speech Recognition service; {0}".format(e))
                        continue

                #### condições de interação ####
                if r.recognize_google(audio, language="pt-BR") == "música": #se ouvir a palavra música, executa a função
                    verificaMusica()
                elif r.recognize_google(audio, language="pt-BR") == "soma":
                    soma()
                elif r.recognize_google(audio,language="pt-BR")=="história":
                    história()
                elif r.recognize_google(audio,language="pt-BR")=="negócios":
                    negocios()
                elif r.recognize_google(audio,language="pt-BR")=="sobre":
                    sobre()
                elif r.recognize_google(audio,language="pt-BR")=="digital":
                    digital()
                elif r.recognize_google(audio,language="pt-BR")=="contato":
                    contato()
                elif r.recognize_google(audio,language="pt-BR")=="setor":
                    setor()
                elif r.recognize_google(audio, language="pt-BR") == "Google":
                    abrirGoogle()
                elif r.recognize_google(audio, language="pt-BR") == "fechar":
                    sair()
                    break
                    
                
