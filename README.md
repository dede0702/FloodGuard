# FloodGuard IoT

O **FloodGuard IoT** é uma solução inovadora para mitigar os impactos das enchentes urbanas, utilizando **sensores inteligentes**, **inteligência artificial** e **comunicação em tempo real** com a população e autoridades públicas.

## 🚀 Visão Geral

O aumento da frequência e intensidade das chuvas nas grandes cidades tem causado grandes prejuízos à população, infraestrutura e economia. A **FloodGuard IoT** busca resolver esse problema por meio de um sistema preventivo, sustentável e inteligente, integrando:

- **Sensores IoT** para monitoramento de pontos críticos de drenagem urbana.
- **Painel de monitoramento em tempo real** para autoridades e equipes de emergência.
- **Alertas automáticos e geolocalizados** via app, SMS e e-mail.
- **Modelos preditivos de IA**, com base em dados meteorológicos e históricos.
- **Fontes de energia renovável**, como painéis solares e baterias de longa duração.

---

### 🚨 Impacto das Enchentes

- **Enchentes no Rio Grande do Sul (Abril-Maio/2024)**:  
  - **183 mortes**  
  - **2,4 milhões de pessoas impactadas**  
  - **Perdas econômicas superiores a R$ 10 bilhões**  
  Fonte: [Wikipédia](https://pt.wikipedia.org/wiki/Enchentes_no_Rio_Grande_do_Sul_em_2024)

- **Enchentes e deslizamentos no Sudeste (Janeiro/2020)**:  
  - **75 mortes**  
  - **Mais de 4 mil desalojados**  
  Fonte: [Wikipédia](https://pt.wikipedia.org/wiki/Enchentes_e_deslizamentos_no_Sudeste_do_Brasil_em_2020)

- **Temporal em São Paulo (Janeiro/2025)**:  
  - **27 mil imóveis sem energia**  
  - **Defesa Civil emitiu alerta severo**  
  Fonte: [UOL Notícias](https://noticias.uol.com.br/cotidiano/ultimas-noticias/2025/01/24/chuvas-em-sao-paulo-janeiro-2025.htm)

---

## 🧠 Tecnologias Utilizadas

O **FloodGuard IoT** combina diversas tecnologias de ponta para garantir eficiência no monitoramento e previsão de enchentes:

- **IoT (Internet das Coisas)**: Sensores distribuídos para monitoramento em tempo real.
- **Machine Learning e IA**: Modelos preditivos para estimar o risco de enchentes.
- **API de Clima**: Integração com dados meteorológicos para previsão de eventos climáticos.
- **React / Next.js**: Utilizados no desenvolvimento do painel de visualização e dashboard.
- **Firebase / AWS / Azure**: Plataformas para a infraestrutura escalável do projeto.
- **n8n / Make / Zapier**: Ferramentas para automações de alertas e integração com outros sistemas.

### 🔮 Modelagem Preditiva com IA (forecast.py)

O módulo **`forecast.py`** contém a lógica responsável pela previsão do risco de enchentes com base em dados de precipitação. Utiliza os seguintes modelos de machine learning:

- **Random Forest**: Usado para prever os níveis de água com base em dados históricos e variáveis temporais (hora, dia, semana).
- **Prophet**: Modelo de séries temporais que analisa tendências e sazonalidades para prever precipitações futuras.

#### **Endpoints da API**:
- **`/predict`** (POST): Retorna as previsões de risco de enchente com base na entrada de dados climáticos.
- **`/train`** (POST): Treina ou re-treina o modelo com dados mais recentes.
- **`/status`** (GET): Verifica o status do modelo ou da API.

### 🛠️ Módulo de Previsão

O modelo preditivo é integrado ao backend da aplicação para fornecer previsões precisas para a população e autoridades. As previsões são feitas com base nas condições meteorológicas e nos dados históricos de precipitação, estimando o risco de enchente (baixo, médio ou alto) para os próximos 6 a 24 horas.

---

## 🛠️ Funcionalidades Principais

- **Sensores de Nível de Água**  
  Monitoramento contínuo dos níveis de água em bueiros e bocas de lobo para detectar possíveis alagamentos.

- **Análise Preditiva com IA**  
  Algoritmos de machine learning que analisam dados climáticos e históricos para prever enchentes com antecedência.

- **Alertas Inteligentes**  
  Notificações em tempo real para moradores e Defesa Civil via aplicativo, SMS e e-mail, com base no risco de enchente identificado.

- **Painel de Monitoramento para Prefeituras**  
  Dashboard intuitivo que permite a visualização de dados em tempo real, ajudando na tomada de decisões rápidas.

- **Energia Sustentável**  
  O sistema é projetado para operar com fontes de energia renováveis, como painéis solares, garantindo maior autonomia e sustentabilidade.

---

## 🌍 Impacto Social e Sustentável

### Alinhamento com os Objetivos de Desenvolvimento Sustentável (ODS):
- **ODS 11** – Cidades e comunidades sustentáveis
- **ODS 13** – Ação contra a mudança global do clima
- **ODS 9** – Indústria, inovação e infraestrutura

---

## 📊 Pesquisa e Validação

O **FloodGuard IoT** foi desenvolvido para atender a uma necessidade urgente de monitoramento e previsão de enchentes, com base em um cenário de desastres recentes e de alto impacto em diversas regiões do Brasil.

---

## 🏙️ Casos de Uso

O sistema **FloodGuard IoT** pode ser utilizado por diversos stakeholders:

- **Prefeituras e Defesa Civil**: Monitoramento de enchentes em tempo real.
- **Empresas de Saneamento**: Prevenção de transbordamentos e danos à infraestrutura.
- **Condomínios e Bairros**: Alertas diretos aos moradores, prevenindo danos e perdas.
- **Seguradoras**: Prevenção de riscos climáticos e redução de perdas financeiras.

---

## 📌 Roadmap

- [x] Prototipagem de sensores IoT
- [x] Integração com API meteorológica (Open-Meteo)
- [ ] MVP funcional com painel web
- [ ] Aplicativo móvel para moradores
- [ ] Programa-piloto com prefeitura parceira
- [ ] Escalonamento para outras cidades

---

## 👥 Integrantes

- **André Rovai Andrade Xavier Junior** - RM555848
- **Renan de França Gonçalves** - RM558413
- **Thiago Almança da Silva** - RM558108

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Se você deseja ajudar com desenvolvimento, testes, UX/UI ou divulgação, entre em contato.

---

## 📬 Contato

Entre em contato com a equipe **FloodGuard IoT**:

- 💎 Email: [em construção]   
- 🌐 Site: [em construção]  
- 📱 Instagram: [em construção]

---

## 📄 Licença

Este projeto está licenciado sob a **MIT License** - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
