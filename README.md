# Amostragem — caderno de estudo

Caderno de estudo autodidata de **Amostragem**, em português, montado a partir de
Bolfarine, H.; Bussab, W. O., *Elementos de Amostragem* (IME-USP, maio de 2004 —
a versão pré-print que circula em PDF; publicado pela Blucher em 2005). Vai do
capítulo 1 (o planejamento de um levantamento, sem fórmulas) e do capítulo 2 (a
formalização: população, amostra, plano amostral, distribuição amostral) aos
dois planos clássicos: amostragem aleatória simples (cap. 3) e estratificada
(cap. 4).

São páginas HTML locais, sem dependência de rede: abrem direto no navegador,
funcionam offline, e a matemática é **MathML nativo** — sem CDN, sem JavaScript
de renderização.

👉 **Comece por [`estudo/index.html`](estudo/index.html).**

## O que já existe

| Cap. | Título | Conteúdo |
|---|---|---|
| 1 | [Noções básicas](estudo/cap01/01-00-nocoes-basicas.html) | Objetivos, constructos, variáveis e parâmetros (média das razões × razão dos totais); unidade elementar, amostral e de resposta; populações **alvo, referida e amostrada** (Fig. 1.1); estratos × subclasses; tipos de investigação e métodos de coleta; o argumento contra a “amostra representativa” e a favor da amostra probabilística; as tipologias de Jessen (Tabela 1.1) e de Kish (Fig. 1.3); AAS, conglomerados, estágios, estratificação, sistemático; estimadores, erro amostral e o exemplo eleitoral (100/400/1600, recalculado); censo × amostra; campo, preparação, análise; erros não amostrais; relatório. 12 cartões de recall e 6 exercícios resolvidos — inclusive o 1.2 (quantas palavras tem o livro?), com amostra sistemática de páginas *e* o censo para conferir. |
| 2 | [Definições e notações básicas](estudo/cap02/02-00-definicoes-e-notacoes-basicas.html) | `U`, `D` e `θ(D)`; `τ`, `μ`, `σ²`, `S²`, `R`, `R̄`; amostras ordenadas, `fᵢ(s)` e `δᵢ(s)`, `n(s)` e `ν(s)`; a Definição 2.5 e os planos A–E do Exemplo 2.6, com as regras de sorteio (AASc, PPT); estatística, distribuição amostral e seus momentos (Tabelas 2.2–2.7 refeitas); `πᵢ` e `πᵢⱼ`; viés, EQM (com a demonstração de EQM = Var + B²); as expressões úteis (2.2)–(2.20), com a demonstração completa de `E[t] = E[f] τ` e `Var[t] = Var[f] N S²`. 12 cartões de recall e 9 exercícios resolvidos (2.1–2.8 e 2.10), com todas as distribuições enumeradas exatamente — inclusive a população de 180 condomínios da Tabela 2.8, transcrita e conferida. |
| 3 | [Amostragem aleatória simples](estudo/cap03/03-00-amostragem-aleatoria-simples.html) | AASc e AASs lado a lado: `fᵢ` Binomial × Bernoulli (Teoremas 3.1 e 3.7, demonstrados), `E[t]`, `Var[t]`, média, estimador expansão, `s²` não viesado para `σ²`/`S²` (a prova via (2.16)–(2.18)); normalidade assintótica, intervalos de confiança, tamanho da amostra (`n = σ²/D`, `1/(D/S² + 1/N)`, total, proporções, conservador); otimalidade de `ȳ` com e sem independência; EPA `(N − n)/(N − 1)`. Tabelas 3.1–3.6 e os Exemplos 3.1–3.7 refeitos, 10 cartões e 13 exercícios resolvidos — inclusive duas amostras reais da Tabela 2.8 (uma delas erra o alvo, e a página explica por quê). |
| 4 | [Amostragem estratificada](estudo/cap04/04-00-amostragem-estratificada.html) | A decomposição `σ² = σ²_d + σ²_e` (demonstrada); o estimador `ȳ_es` e o Teorema 4.1 para qualquer plano dentro dos estratos; alocações proporcional (`V_pr = σ²_d/n`), uniforme e ótima de Neyman por Cauchy–Schwarz; `V_ot ⩽ V_pr ⩽ V_c` e a leitura de (4.25); EPA; IC, tamanho da amostra e proporções. Exemplos 4.1–4.4 conferidos, um diagrama da população estratificada, 10 cartões e 15 exercícios — com a enumeração completa de `S_AASs` (70 amostras) contra `S_AEun` (30) na população de oito. |

Além das aulas há **duas folhas de consulta**, cada uma condensando os quatro
capítulos em cinco páginas A4 de duas colunas, para levar impressas (Ctrl+P →
“Salvar como PDF”):

- **[Guia de prova](estudo/guia/01-04-guia-de-prova.html)** — o guia de
  trabalho: mapa de decisão “o que a questão pede × que ferramenta usar”, os
  enunciados e as contas, um exemplo numérico por ideia, “fato ou fake”,
  checklist, fórmulas de bolso, o mínimo em R e um glossário de símbolos.
- **[Definições e resultados](estudo/guia/01-04-definicoes-e-resultados.html)** —
  só os enunciados: toda definição, teorema, corolário e lema dos quatro
  capítulos, na numeração do livro e **com as hipóteses que cada um exige**,
  fechando num quadro “resultado × o que exige × quando quebra”.

## Como as aulas são organizadas

Cada capítulo é uma página dividida em **12 passos**, cada um do tamanho de uma
tela:

- abre com **a ideia em uma linha** — a conclusão vem antes do desenvolvimento;
- traz o **caso numérico à esquerda e o símbolo à direita**, lado a lado e
  sempre nessa ordem;
- mostra as contas em **lista numerada**, uma operação por linha;
- e termina com **uma pergunta de recuperação**, com a resposta escondida.

No fim há um **fecho**: fechar a página e escrever o capítulo inteiro de
memória, de uma vez só, conferindo depois contra uma lista de 12 itens. Só
então vêm os **exercícios resolvidos** com gabarito comentado.

Ainda há figuras do livro e diagramas redesenhados, código em **R** com a
saída, e as definições, resultados e demonstrações em caixas de cores
distintas. **Todo resultado numérico foi recalculado**, não copiado — e as
divergências com o impresso estão anotadas no fim de cada página.

## Estrutura

```
├── index.html              redireciona para estudo/
├── estudo/
│   ├── index.html          painel do percurso
│   ├── assets/
│   │   ├── tema.css        cores, fontes e medidas (tema azul-cobalto)
│   │   ├── estilo.css      estrutura e layout das aulas
│   │   ├── aula.css        o formato em 12 passos
│   │   └── guia.css        layout da folha de consulta (A4, duas colunas)
│   ├── capNN/
│   │   ├── NN-00-titulo.html
│   │   └── img/            figuras recortadas do PDF
│   └── guia/
│       ├── 01-04-guia-de-prova.html            folha de consulta, caps. 1 a 4
│       └── 01-04-definicoes-e-resultados.html  enunciados e hipóteses
└── ferramentas/
    ├── extrair.py          texto (com os acentos do TeX recompostos), páginas e recortes do PDF
    └── figuras.py          detecção automática de figuras
```

Trocar de tema é trocar `assets/tema.css`: todas as cores e medidas do site
estão ali, em variáveis CSS, e `estilo.css` nunca traz cor literal. Há suporte a
modo claro e escuro pelo `prefers-color-scheme`.

## Sobre o PDF do livro

O PDF **não** está no repositório — é obra protegida por direitos autorais. As
ferramentas o localizam sozinhas se você colocar a sua própria cópia na raiz da
pasta. É um PDF nativo gerado por pdfTeX: a camada de texto existe, mas os
acentos vêm separados das letras (“S˜ao”, “Matem´atica”); `extrair.py` os
recompõe. A numeração é constante, **página do PDF = página do livro + 12**.

## Uso das ferramentas

```bash
python ferramentas/extrair.py texto --livro 37 60        # texto pela numeração do livro
python ferramentas/extrair.py recorte 22 186 128 514 613 fig.png
python ferramentas/extrair.py buscar "Horwitz"
python ferramentas/figuras.py listar 22
```

Requer Python 3 e `pymupdf`. No Windows, para redirecionar a saída de `texto`
para arquivo, use `PYTHONIOENCODING=utf-8`.

## Aviso

Material de estudo pessoal. As páginas reproduzem figuras, tabelas e enunciados
da obra original para fins de estudo; todas trazem `noindex, nofollow` e o
repositório inclui um `robots.txt` restritivo. Não é substituto do livro — é um
caderno de quem está lendo o livro.
