# API de Dados Úteis - Dashboard Interativo

Uma API robusta e um dashboard moderno para consulta de CEP, clima e cotações de moedas em tempo real.

## 🚀 Funcionalidades

### Backend (FastAPI)
- **Consulta de CEP**: Busca endereços por CEP em todo o Brasil
- **Previsão do Tempo**: Dados meteorológicos em tempo real
- **Cotação de Moedas**: Cotações atualizadas de diversas moedas

### Frontend (Dashboard Interativo)
- **Interface Moderna**: Design responsivo com animações suaves
- **Sistema de Cache**: Melhora performance e reduz requisições
- **Validação Robusta**: Validação em tempo real dos dados
- **Notificações Toast**: Feedback visual para o usuário
- **Estatísticas em Tempo Real**: Monitoramento de consultas e performance
- **Geolocalização**: Obtenção automática de coordenadas
- **Sistema de Retry**: Tentativas automáticas em caso de falha
- **Exportação de Dados**: Funcionalidade para exportar dados

## 🛠️ Tecnologias

### Backend
- **FastAPI**: Framework web moderno e rápido
- **Python 3.8+**: Linguagem principal
- **Requests**: Para requisições HTTP
- **Uvicorn**: Servidor ASGI

### Frontend
- **HTML5/CSS3**: Estrutura e estilização
- **JavaScript ES6+**: Lógica da aplicação
- **Font Awesome**: Ícones
- **Google Fonts**: Tipografia moderna
- **CSS Variables**: Sistema de design consistente

## 📦 Instalação

### Pré-requisitos
- **Python 3.8+** instalado no sistema
- **Git** (opcional, para clonar o repositório)

### Instalação do Python (Windows)
Se você não tem Python instalado:

1. **Opção 1 - Microsoft Store (Recomendado):**
   - Abra o Microsoft Store
   - Procure por "Python 3.11" ou "Python 3.12"
   - Clique em "Instalar"

2. **Opção 2 - Site oficial:**
   - Acesse https://python.org
   - Baixe a versão mais recente
   - **Importante:** Marque "Add Python to PATH" durante a instalação

### Executando o Projeto

#### Método 1: Script Automático (Recomendado)
```bash
# Execute o script batch
run_server.bat

# Ou execute o script PowerShell
.\run_server.ps1
```

#### Método 2: Comando Manual
```bash
# 1. Instalar dependências
pip install -r requirements.txt

# 2. Executar servidor
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Se python não funcionar, tente:
py -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

#### Método 3: Usando o arquivo main.py
```bash
python main.py
```

### Acessando o Dashboard
Após executar o servidor, acesse:
```
http://localhost:8000/static/index.html
```

### Solução de Problemas

**Problema:** "Python não foi encontrado"
**Soluções:**
1. Instale Python do Microsoft Store
2. Verifique se Python está no PATH
3. Use `py` em vez de `python`
4. Execute o script `run_server.bat` que detecta automaticamente

## 🎯 Funcionalidades Avançadas

### Sistema de Cache
- Cache inteligente para CEP (10 minutos)
- Cache para clima (5 minutos)
- Cache para moedas (1 minuto)
- Persistência no localStorage

### Validação Robusta
- Validação de CEP (8 dígitos)
- Validação de coordenadas (latitude/longitude)
- Feedback visual em tempo real
- Tratamento de erros elegante

### Performance
- Requisições com retry automático
- Timeout configurável
- Backoff exponencial
- Monitoramento de tempo de resposta

### UX/UI Melhorada
- Animações suaves
- Estados de loading
- Notificações toast
- Design responsivo
- Atalhos de teclado

## 🔧 Configuração

### Variáveis de Ambiente
```bash
# Configurações da API (opcional)
API_TIMEOUT=10000
API_RETRY_ATTEMPTS=3
```

### Personalização
O dashboard pode ser personalizado através das variáveis CSS:
```css
:root {
    --primary-color: #667eea;
    --secondary-color: #764ba2;
    --success-color: #4CAF50;
    --warning-color: #FF9800;
    --error-color: #f44336;
}
```

## 📊 Endpoints da API

### CEP
```
GET /cep/{cep}
```
Retorna dados do endereço para o CEP informado.

### Clima
```
GET /clima?lat={latitude}&lon={longitude}
```
Retorna dados meteorológicos para as coordenadas informadas.

### Moeda
```
GET /moeda/{par}
```
Retorna cotação do par de moedas informado.

## 🎨 Melhorias do Frontend

### Design System
- **Tipografia**: Fonte Inter para melhor legibilidade
- **Cores**: Sistema de cores consistente com variáveis CSS
- **Espaçamento**: Grid system responsivo
- **Animações**: Transições suaves e feedback visual

### Funcionalidades Avançadas
- **Dashboard de Estatísticas**: Monitoramento em tempo real
- **Sistema de Toast**: Notificações não intrusivas
- **Geolocalização**: Obtenção automática de coordenadas
- **Cache Inteligente**: Reduz requisições desnecessárias
- **Validação em Tempo Real**: Feedback imediato ao usuário

### Performance
- **Lazy Loading**: Carregamento sob demanda
- **Debounce**: Evita requisições excessivas
- **Retry Automático**: Recuperação de falhas
- **Cache Local**: Persistência de dados

## 🚀 Como Usar

1. **Consulta de CEP**:
   - Digite o CEP no formato 00000-000
   - Pressione Enter ou clique em "Buscar CEP"

2. **Consulta de Clima**:
   - Digite latitude e longitude
   - Ou use "Usar Minha Localização"
   - Clique em "Consultar Clima"

3. **Consulta de Moedas**:
   - Selecione o par de moedas
   - Clique em "Consultar Cotação"

## 🔍 Debug e Desenvolvimento

### Console do Navegador
```javascript
// Acessar funções de debug
window.debug.limparCache()
window.debug.exportarDados()
window.debug.verificarStatusAPI()
```

### Atalhos de Teclado
- `Ctrl/Cmd + Enter`: Executar consulta ativa
- `Enter`: Executar consulta no campo focado

## 📈 Monitoramento

O dashboard inclui:
- **Contador de consultas**: Total de consultas do dia
- **Tempo médio de resposta**: Performance da API
- **Status da API**: Online/Offline em tempo real

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## 🆕 Changelog

### v2.0.0 - Dashboard Interativo
- ✨ Interface completamente redesenhada
- 🚀 Sistema de cache inteligente
- 📊 Dashboard de estatísticas
- 🔔 Sistema de notificações toast
- 📱 Design totalmente responsivo
- ⚡ Performance otimizada
- 🛡️ Validação robusta
- 🔄 Sistema de retry automático
- 📍 Geolocalização integrada
- 🎨 Animações e transições suaves

### v1.0.0 - Versão Inicial
- 🌐 API básica com FastAPI
- 📍 Consulta de CEP
- 🌤️ Consulta de clima
- 💰 Consulta de moedas
- �� Interface simples
