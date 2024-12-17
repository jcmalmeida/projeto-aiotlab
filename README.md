
# **Projeto AIoT Lab**

Este é um projeto baseado em **Flask**, servindo como uma aplicação prática para o gerenciamento e visualização de imagens processadas. Este projeto utiliza **Docker** e **Nginx** para escalabilidade e robustez.


## **Recursos do Projeto**

- **Interface Web**:
  - Upload de imagens com processamento automático.
  - Visualização de imagens originais e processadas.

- **Processamento de Imagens**:
  - Aplicação de filtros e transformações usando **OpenCV**.

- **Persistência**:
  - Armazenamento de registros no banco de dados SQLite.
  - Persistência de imagens processadas e originais.

- **Infraestrutura**:
  - Gerenciado por **Docker** e **Docker Compose**.
  - Servidor **Flask** para backend e **Nginx** como proxy reverso.


## **Requisitos**

Certifique-se de ter os seguintes softwares instalados:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)


## **Como Rodar o Projeto**

### **1. Clone o Repositório**
```bash
git clone https://github.com/jcmalmeida/projeto-aiotlab.git
cd projeto-aiotlab
```

### **2. Suba os Contêineres com Docker Compose**
```bash
docker-compose up --build
```

- O serviço Flask estará disponível em `http://localhost`.
- O Nginx estará escutando na porta 80.


## **Funcionalidades Principais**

1. **Upload de Imagens**:
   - Carregue imagens pela interface web e visualize o processamento automático.

2. **Gerenciamento de Registros**:
   - Visualize os registros com informações de **Data/Hora**, **Imagens Originais** e **Imagens Processadas**.

3. **Logs e Monitoramento**:
   - **Logs do Nginx** persistem em `./logs/nginx`.
   - Registros do Flask disponíveis via `docker logs flask_app`.


## **Estrutura do Projeto**

```
projeto-aiotlab/
├── app/
│   ├── app.py                  # Backend Flask
│   ├── requirements.txt        # Dependências do Python
│   ├── nginx.conf              # Configuração do Nginx
│   ├── Dockerfile              # Dockerfile do Flask
│   ├── database/               # Banco de dados SQLite
│   ├── static/                 # Arquivos estáticos (imagens, CSS, JS)
│   │   ├── uploads/            # Armazenamento de imagens
│   ├── templates/              # Arquivos HTML (frontend)
├── docker-compose.yml          # Gerenciamento dos contêineres
├── README.md                   # Documentação
```


## **APIs Disponíveis**

### **1. Upload de Imagens**
**Endpoint**: `/upload`  
**Método**: `POST`  
**Descrição**: Envia uma imagem para processamento e armazenamento.

**Exemplo de Resposta**:
```json
{
  "datetime": "2024-12-16 14:35:00",
  "image": "static/uploads/original.jpg",
  "image_proc": "static/uploads/original_processed.jpg",
  "ip": "127.0.0.1"
}
```

### **2. Obtenção dos registros de processamento realizados**
**Endpoint**: `/registros`  
**Método**: `GET`  
**Descrição**: Obtém os dados dos registros enviados e processados.

**Exemplo de Resposta**:
```json
[
  {
    "id": 1,
    "datetime": "2024-06-16 14:35:00",
    "image": "static/uploads/img1.jpg",
    "image_proc": "static/uploads/img1_processed.jpg",
    "ip": "192.168.1.10"
  },
  {
    "id": 2,
    "datetime": "2024-06-16 14:40:00",
    "image": "static/uploads/img2.jpg",
    "image_proc": "static/uploads/img2_processed.jpg",
    "ip": "192.168.1.11"
  }
]

```


## **Tecnologias Utilizadas**

- **Linguagem**: Python (Flask)
- **Processamento de Imagens**: OpenCV
- **Banco de Dados**: SQLite
- **Gerenciamento de Contêineres**: Docker & Docker Compose
- **Servidor Web**: Nginx
