from random import choice, randint
import sqlite3
from main import tela

conn = sqlite3.connect('db/data.db')
c = conn.cursor()
tela.lb_status_conexao.setText('Conectado com sucesso!')

def gerar():
    n = choice(nomes)
    sn_1 = choice(sobrenomes)
    sn_2 = choice(sobrenomes)
    s_total = f"{sn_1} {sn_2}"

    # TELEFONES
    tel = randint(960000000, 999999999)

    # DATA DE NASCIMENTO
    dia = randint(1, 29)
    mes = randint(1, 12)
    ano = randint(1920, 2021)
    dt = f'{dia}.{mes}.{ano}'

    c.execute(f"INSERT INTO CONTATINHOS (NOME,TEL,DT_NASC) VALUES ('{n} {s_total}','{tel}','{dt}')")
    c.execute("COMMIT;")


sobrenomes = ['Abreu', 'Adães', 'Adorno', 'Aguiar', 'Albuquerque', 'Alcântara', 'Aleluia', 'Alencar', 'Almeida',
              'Altamirano', 'Alvarenga',
              'Álvares', 'Alves', 'Alvim', 'Amaral', 'Amigo', 'Amor', 'Amorim', 'Anchieta', 'Andrada', 'Andrade',
              'Anes', 'Anjos', 'Antunes',
              'Anunciação', 'Aragão', 'Araújo', 'Arruda', 'Ascensão', 'Assis', 'Azeredo', 'Azevedo', 'Bandeira',
              'Barbosa', 'Barros', 'Barroso',
              'Bastos', 'Batista', 'Bermudes', 'Bernades', 'Bernardes', 'Bicalho', 'Bispo', 'Bocaiuva', 'Bolsonaro',
              'Borba', 'Borges', 'Borsoi',
              'Botelho', 'Braga', 'Bragança', 'Brandão', 'Brasil', 'Brasiliense', 'Bueno', 'Cabral', 'Café', 'Camacho',
              'Camargo', 'Caminha',
              'Camões', 'Cardoso', 'Carmo', 'Carnaval', 'Carneiro', 'Carvalhal', 'Carvalho', 'Carvalhosa', 'Castilho',
              'Castro', 'Cerejeira',
              'Chaves', 'Coelho', 'Coentrão', 'Coimbra', 'Constante', 'Cordeiro', 'Costa', 'Cotrim', 'Couto',
              'Coutinho', 'Cruz', 'Cunha', 'Curado',
              'Dambros', 'Dias', 'Diegues', 'Dorneles', 'Duarte', 'Eça', 'Encarnação', 'Esteves', 'Evangelista',
              'Exaltação', 'Fagundes',
              'Faleiros', 'Falópio', 'Falqueto', 'Faria', 'Farias', 'Faro', 'Ferrão', 'Ferraz', 'Ferreira', 'Ferrolho',
              'Fernandes', 'Figo',
              'Figueira', 'Figueiredo', 'Figueiroa', 'Fioravante', 'Fonseca', 'Fontes', 'Fortaleza', 'França', 'Freire',
              'Freitas', 'Frota',
              'Furquim', 'Furtado', 'Galvão', 'Gama', 'Garrastazu', 'Gato', 'Gomes', 'Gonçales', 'Gonçalves', 'Gonzaga',
              'Gouveia', 'Guimarães',
              'Gusmão', 'Henriques', 'Hernandes', 'Holanda', 'Homem', 'Hora', 'Hungria', 'Jardim', 'Junqueira',
              'Lacerda', 'Lange', 'Leitão',
              'Leite', 'Leme', 'Lins', 'Locatelli', 'Lopes', 'Luz', 'Macedo', 'Machado', 'Madureira', 'Maduro',
              'Magalhães', 'Mairinque',
              'Malafaia', 'Malta', 'Mariz', 'Marques', 'Martins', 'Massa', 'Matos', 'Médici', 'Meireles', 'Mello',
              'Melo', 'Mendes', 'Mendonça',
              'Menino', 'Mesquita', 'Miranda', 'Moraes', 'Morais', 'Morato', 'Moreira', 'Moro', 'Monteiro', 'Muniz',
              'Namorado', 'Nantes',
              'Nascimento', 'Navarro', 'Naves', 'Negreiros', 'Negrete', 'Neves', 'Nóbrega', 'Nogueira', 'Noronha',
              'Nunes', 'Oliva', 'Oliveira',
              'Outeiro', 'Pacheco', 'Padrão', 'Paes', 'Pais', 'Paiva', 'Paixão', 'Papanicolau', 'Parga', 'Pascal',
              'Pascoal', 'Pasquim', 'Patriota',
              'Peçanha', 'Pedrosa', 'Pedroso', 'Peixoto', 'Pensamento', 'Penteado', 'Pereira', 'Peres', 'Pessoa',
              'Pestana', 'Pimenta', 'Pimentel',
              'Pinheiro', 'Pinto', 'Pires', 'Poeta', 'Policarpo', 'Porto', 'Portugal', 'Prado', 'Prudente', 'Quaresma',
              'Queirós', 'Queiroz',
              'Ramalhete', 'Ramalho', 'Ramires', 'Ramos', 'Rangel', 'Reis', 'Resende', 'Ribeiro', 'Rios', 'Rodrigues',
              'Roma', 'Romão', 'Sá',
              'Sacramento', 'Sampaio', 'Sampaulo', 'Sampedro', 'Sanches', 'Santacruz', 'Santana', 'Santander',
              'Santarrosa', 'Santiago',
              'Santos', 'Saragoça', 'Saraiva', 'Saramago', 'Seixas', 'Serra', 'Serrano', 'Silva', 'Silveira', 'Simões',
              'Siqueira', 'Soares',
              'Soeiro', 'Sousa', 'Souza', 'Tavares', 'Teixeira', 'Teles', 'Torquato', 'Trindade', 'Uchoa', 'Uribe',
              'Ustra', 'Valadares', 'Valença',
              'Valente', 'Varela', 'Vasconcelos', 'Vasques', 'Vaz', 'Veiga', 'Velasques', 'Veloso', 'Viana', 'Vieira',
              'Vilela', 'Vilhena',
              'Xavier', 'Zampo']
nomes = ['José', 'Jose', 'João', 'Antônio', 'Antonio', 'Francisco', 'Carlos', 'Paulo', 'Pedro', 'Lucas', 'Luiz', 'Luíz',
         'Marcos', 'Luis', 'Luís',
         'Gabriel', 'Rafael', 'Daniel', 'Marcelo', 'Bruno', 'Eduardo', 'Felipe', 'Raimundo', 'Rodrigo', 'Maria', 'Ana',
         'Francisca', 'Antônia', 'Antonia',
         'Adriana', 'Juliana', 'Márcia', 'Marcia', 'Fernanda', 'Patricia', 'Patrícia', 'Aline', 'Sandra', 'Camila',
         'Amanda', 'Bruna', 'Jéssica', 'Jessica',
         'Leticia', 'Letícia', 'Júlia', 'Julia', 'Luciana', 'Vanessa', 'Mariana']




