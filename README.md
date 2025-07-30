# API de Dados Úteis

Uma API completa com interface web moderna para consultar CEP, clima e cotações de moedas.

## 🚀 Funcionalidades

- **Consulta de CEP**: Busca informações completas de endereços pelo CEP
- **Previsão do Tempo**: Consulta clima atual por coordenadas geográficas
- **Cotação de Moedas**: Obtém cotações em tempo real de diversas moedas

## 🛠️ Tecnologias

- **Backend**: FastAPI (Python)
- **Frontend**: HTML, CSS, JavaScript
- **APIs Externas**: ViaCEP, Open-Meteo, AwesomeAPI

## 📦 Instalação

1. Clone o repositório:
```bash
git clone <seu-repositorio>
cd api_dados_uteis
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute o servidor:
```bash
uvicorn main:app --reload
```

4. Acesse a interface web:
```
http://localhost:8000/static/index.html
```

## 🎯 Como Usar

### Interface Web
Acesse `http://localhost:8000/static/index.html` para usar a interface gráfica que inclui:

- **Consulta de CEP**: Digite um CEP válido (ex: 01001-000)
- **Previsão do Tempo**: Insira latitude e longitude (ex: -23.5505, -46.6333 para São Paulo)
- **Cotação de Moedas**: Selecione o par de moedas desejado

### API REST
Você também pode usar diretamente as APIs:

```bash
# Consultar CEP
GET http://localhost:8000/cep/01001000

# Consultar clima
GET http://localhost:8000/clima?lat=-23.5505&lon=-46.6333

# Consultar cotação de moeda
GET http://localhost:8000/moeda/USD-BRL
```

## 📊 APIs Utilizadas

- **ViaCEP**: Consulta de CEPs brasileiros
- **Open-Meteo**: Previsão do tempo gratuita
- **AwesomeAPI**: Cotações de moedas em tempo real

## 🤝 Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 🆘 Suporte

Se você encontrar algum problema ou tiver sugestões, abra uma issue no repositório.

---

**Desenvolvido com FastAPI, JavaScript e IA**
