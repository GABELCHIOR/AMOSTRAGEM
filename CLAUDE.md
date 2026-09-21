# AMOSTRAGEM — Bolfarine & Bussab, Elementos de Amostragem

Projeto de estudo autodidata de Amostragem (populações finitas).
Toda a produção é **em português (pt-BR)**.

Este projeto é irmão do `ESTOCASTICOS` (Ross), do `MULTI` (Johnson & Wichern)
e do `PP_estudo` (Montgomery): mesma estrutura, mesmo CSS, mesmo formato de
aula. Diferenças: o tema é **azul-cobalto**, e — como no ESTOCASTICOS — há
**três caixas matemáticas coloridas** (resultado / demonstração / exemplo),
com a caixa de resultado em **petróleo** (não índigo, para não brigar com o
azul do tema).

## O livro

- Arquivo: `elementos-de-amostragem.pdf` (1,4 MB, 281 páginas)
- Bolfarine, H.; Bussab, W. O. — **Elementos de Amostragem**, IME-USP, maio de
  2004 (pré-print em pdfTeX; a edição impressa é Blucher, 2005)
- 11 capítulos + apêndices A (palavras-chave, p. 261) e B (tópicos para um
  levantamento, p. 265) + referências

**É um PDF nativo de pdfTeX, sem bookmarks.** A camada de texto existe, mas os
**acentos vêm separados das letras** (“S˜ao”, “Matem´atica”, “¸c˜ao”) e o “i”
acentuado vem como i-sem-pingo + acento. `ferramentas/extrair.py::limpar()`
recompõe tudo; todo comando de texto passa por ela. As fórmulas saem com as
quebras do TeX (frações e somatórios empilhados) — bastam para localizar e
conferir. As tabelas saem com as células em linhas separadas e **os brancos da
Tabela 2.8 (= zeros) somem no texto**: para tabelas numéricas, extrair por
coordenadas com `page.get_text("words")` e atribuir cada número à coluna pela
borda direita (`x1`), como se fez para a Tabela 2.8.

**Offset constante: página do PDF = página do livro + 12.** Use
`livro2pdf()` / `pdf2livro()` de `ferramentas/extrair.py` mesmo assim.

| Cap. | Título | Livro p. | PDF p. | Status |
|---|---|---|---|---|
| 1 | Noções básicas | 1 | 13 | ✅ `estudo/cap01/01-00-nocoes-basicas.html` |
| 2 | Definições e notações básicas | 37 | 49 | ✅ `estudo/cap02/02-00-definicoes-e-notacoes-basicas.html` |
| 3 | Amostragem aleatória simples | 61 | 73 | ✅ `estudo/cap03/03-00-amostragem-aleatoria-simples.html` |
| 4 | Amostragem estratificada | 93 | 105 | ✅ `estudo/cap04/04-00-amostragem-estratificada.html` |
| 5 | Estimadores do tipo razão | 127 | 139 | — |
| 6 | Estimadores do tipo regressão | 145 | 157 | — |
| 7 | Amostragem por conglomerados em um estágio | 159 | 171 | — |
| 8 | Amostragem em dois estágios | 197 | 209 | — |
| 9 | Estimação com probabilidades desiguais | 225 | 237 | — |
| 10 | Resultados assintóticos | 239 | 251 | — |
| 11 | Exercícios complementares | 249 | 261 | — |
| A | Relação de palavras-chave | 261 | 273 | referência |
| B | Tópicos para um levantamento amostral | 265 | 277 | referência |

## Preferências de estudo definidas

| Item | Decisão |
|---|---|
| Objetivo | Disciplina de Amostragem. Percurso **desde o cap. 1**, porque o vocabulário (unidade elementar/amostral, populações alvo/referida/amostrada, estrato × subclasse) e a atitude (amostra probabilística, não “representativa”) são cobrados. Ênfase em entender de onde vem cada resultado. |
| Demonstrações | Manter as que agregam: as que passam por `fᵢ`/`δᵢ`, simetria do plano, tamanho fixo, (2.4). Pura álgebra fica resumida na prosa. |
| Caixas | Definições em `.caixa.definicao` (neutra, filete petróleo — é a caixa mais frequente deste livro); resultados/identidades numeradas em `.caixa.teorema` (petróleo, fundo tingido); demonstrações em `.caixa.demonstracao` (verde-musgo); exemplos em `.caixa.exemplo` (âmbar). Avisos em `.caixa.aviso` (castanho-queimado). |
| Exemplos e exercícios | Selecionar os mais relevantes; no cap. 2, **enumerar `S_A` por completo** para cada plano e conferir cada fração. Os exercícios do cap. 1 são de discussão; as respostas são minhas (o livro não traz gabarito). |
| Software | **R**, funções de base. Padrão do cap. 2: `expand.grid`/`combn` para listar as amostras, vetor `p` de probabilidades e somas ponderadas para `E`, `Var`, `Cov`. |
| Formato | **Arquivos HTML locais** em `estudo/`. Offline. Matemática em **MathML nativo** (sem CDN, sem JS). |
| Idioma | Português (pt-BR). Termos técnicos com o original em inglês entre parênteses na primeira ocorrência quando o livro o faz (survey, checklist, peoplemeter). |

## Como trabalhar aqui

**Geração sob demanda, capítulo por capítulo.** A cada sessão o usuário escolhe
o próximo capítulo e eu gero uma página de estudo focada.

Cada página contém, nesta ordem:

1. **Objetivo da aula** — o que se deve saber fazer ao final
2. **Conceito** em português, com a matemática em MathML; definições,
   resultados, demonstrações e exemplos nas caixas
3. **Figuras** recortadas do PDF e **diagramas em SVG inline**
   (`<figure class="diagrama">`, cores via variáveis do tema)
4. **Exemplos do livro resolvidos passo a passo**, com o código em R e a saída
5. **Cartões de recall ativo** — pergunta com resposta escondida (`<details>`)
6. **Exercícios selecionados** do fim do capítulo, com gabarito comentado

**Tom das aulas:** professor dando aula, não resumo. Explicar o *porquê*,
mostrar as derivações, ligar cada conceito a onde ele reaparece nos capítulos
seguintes.

**Regra dos números:** todo resultado numérico é *calculado* (Python com
`fractions.Fraction` no scratchpad, para as distribuições amostrais; numpy para
o resto), nunca copiado de memória, e conferido contra o livro. As saídas de R
nas páginas são escritas à mão a partir dos números conferidos em Python —
**R não está instalado no PATH**. Mantê-las simples, com poucas casas. Para
simulações (`rnorm`, `set.seed`) **não inventar saída**: mostrar só o código
e dizer o que esperar.

**Divergências encontradas no livro:**

- Cap. 1, p. 21, exemplo eleitoral: o intervalo para n = 1600 sai impresso
  “53,5% a 59,5%”; o correto é 53,6%–58,4% (meia-largura 2,4 pontos). Anotado
  na `.nota` do cap. 1.
- Cap. 2, Ex. 2.7: a fórmula de `P(s)` repete “se i ∈ s” por erro de
  composição; leia “1/9 se s ∈ S₂”. Anotado.
- Cap. 2, Ex. 2.14: EQM impresso 0,6458 (viés arredondado 0,13 ao quadrado);
  exato 97/150 = 0,6467. Anotado.
- Cap. 3: nos tamanhos de amostra o livro usa z ≈ 2 (D = B²/4) e nos
  intervalos 1,96 (Ex. 3.2: n = 96 com z = 2, 93 com 1,96; Ex. 3.6: 3466 vs
  3341). Segui o livro nos exemplos, 1,96 nos exercícios. Ex. 3.3: limite
  inferior −0,061, impresso 0,00. Ex. 3.9(c) fala em "residentes" (herança do
  3.4); tomei Y > 3. Ex. 3.6: o estimador pedido é viesado (E = 4 ≠ 4,5).
- Cap. 4, (4.19): impresso com os dois fatores iguais a Σ W_h σ_h/√c_h; o
  correto é (Σ W_h σ_h √c_h)(Σ W_h σ_h/√c_h)/V_es. Anotado. Ex. 4.1 dá S²_h e
  as fórmulas AASc pedem σ²_h: converti por (N_h − 1)/N_h.

**Números conferidos que valem reutilizar:** Tabela 2.8 (180 condomínios):
τ_Y = 3363, μ_Y = 18,683, S²_Y = 409,75; τ_X = 4928, μ_X = 27,378,
S²_X = 609,41; P(Y > 20) = 58/180; ρ_XY = 0,962; R = 0,6824. Os vetores `Y` e
`X` em R estão no Exercício 2.2 do cap. 2 — copiar de lá para os caps. 3, 5 e 6.
Exercício 1.2: o livro tem 58 500 palavras nas 269 páginas numeradas (critério:
token com ao menos uma letra, no texto do PDF).
Tabela 2.8 por estratos de 60 (ordem da lista): μ_h = 28,57, 20,80, 6,68;
σ²_h = 544,8, 326,3, 105,1; σ²_d = 325,4, σ²_e = 82,1 (Ex. 4.9).
População do Ex. 4.1 (D = 13,17,6,5,10,12,19,6): μ = 11, σ² = 24, S² = 192/7.
**Amostras "sorteadas" nos exercícios 3.9 e 4.9:** índices gerados em Python
(`numpy.random.default_rng(2004)`, `integers(1, 181, n)`) e listados
explicitamente no código R da página — reproduzível sem R.

**Ganchos plantados (retomar quando o capítulo chegar):**

- estimador expansão `T = nȳ + (N − n)ȳ`: "a parte não observada é estimada
  por ȳ" → razão e regressão substituem ȳ por uma previsão, **caps. 5 e 6**
- Ex. 3.7 (dentistas) = pós-estratificação / estimador razão com X = 140
  conhecido → **cap. 5**; Ex. 3.5/3.41 (`ȳ_c`) = usar informação auxiliar
  bate ȳ fora da classe linear → **caps. 5 e 6**
- `r` viesado, `E[f̄]` não viesada só em planos simétricos → **cap. 5**
- Ex. 4.6/4.27: `ȳ_m` (média simples de amostra estratificada) é viesado; o
  Ex. 3.6 é um caso → pesos amostrais, **caps. 8 e 9**
- EPA (cap. 3, `(N−n)/(N−1)`; cap. 4, `1 − σ²_e/σ²`) → perda dos conglomerados
  e correlação intraclasse, **cap. 7**
- Ex. 4.16 (estágios dentro de estratos, PPT) ficou de fora — retomar no
  **cap. 8/9**
- correlação intraclasse mencionada nos exercícios 1.10 e 1.12 → **cap. 7**
- `π_i`, `π_ij`, e o `π_13 = 0` do plano E → Horvitz–Thompson, **cap. 9**
- (2.19)–(2.20) (esperança e variância iteradas) → **cap. 8**
- sistemático como conglomerado único, sem estimativa de variância → **7.8**

## Ferramentas

`ferramentas/extrair.py` — localiza o PDF sozinho na raiz (prioridade ao nome
que contém "amostra"), recompõe os acentos (`limpar`) e converte a numeração
com `livro2pdf`/`pdf2livro`. Redirecionar a saída de `texto` para arquivo
quebra no Windows (`cp1252`): use `PYTHONIOENCODING=utf-8`. `sumario` avisa
que o PDF não tem bookmarks (o sumário impresso está nas PDF p. 3–7).
`ferramentas/figuras.py` — copiado do ESTOCASTICOS; aglomera os traçados
vetoriais da página em caixas.

```bash
python ferramentas/extrair.py texto --livro 61 92
python ferramentas/extrair.py recorte 22 186 128 514 613 fig.png
python ferramentas/extrair.py buscar "Neyman"
python ferramentas/figuras.py listar 22
```

Dependências: `pymupdf` (instalado). Python 3.13.

Figuras: o cap. 1 tem três. A Fig. 1.1 (PDF p. 22, recorte `186 128 514 613`)
foi recortada; as Figs. 1.2 e 1.3 são árvores desenhadas com `\put` do TeX e
saem como lixo no texto — foram **redesenhadas em SVG** com as classes `.cx`,
`.cx-folha`, `.ramo`, `.tx`, `.tx-crit` de `estilo.css`. Cap. 2 não tem
figuras, só tabelas (refeitas em HTML). Cap. 3 idem. Cap. 4 só tem a Tabela
4.1; desenhei em SVG a população do Ex. 4.1 com `<tspan baseline-shift="sub">`
para os subíndices.

## Convenção de nomes

Igual ao MULTI. **Números sempre com dois dígitos**, minúsculas, sem acento,
hífen entre palavras.

| O quê | Padrão | Exemplo |
|---|---|---|
| Pasta do capítulo | `capNN/` | `cap02/` |
| Página do capítulo inteiro | `NN-00-titulo.html` | `cap02/02-00-definicoes-e-notacoes-basicas.html` |
| Figura | `img/fig-NN-MM.png` | `cap01/img/fig-01-01.png` |

Ao criar uma aula nova, acrescentar o link em **três** lugares de
`estudo/index.html`: a lista da barra lateral (trocar o `<li class="adiante">`
por um `<li>` com link), o cartão em "Aulas disponíveis" (trocar o
`<span class="cartao pendente">` por `<a class="cartao">`) e a linha da tabela
da seção **"Menu"**. E acertar o `.nav-rodape` (anterior/próxima) da aula
vizinha — o do cap. 4 hoje diz "Cap. 5 … (em breve)" sem link.

## Layout das páginas

O CSS está separado em dois arquivos e essa separação é para valer:

- `estudo/assets/tema.css` — **única** fonte de cores, fontes e medidas, com
  bloco `@media (prefers-color-scheme: dark)`. Tema: **azul-cobalto**. Regra
  geral: superfícies neutras, cor só em tipografia e filetes. **Exceção:** as
  variáveis `--teorema/--teorema-fundo` (petróleo), `--demo/--demo-fundo`,
  `--exemplo/--exemplo-fundo` dão fundo tingido às três caixas matemáticas.
  `--ambar` (avisos) aqui é castanho-queimado, porque o âmbar de verdade ficou
  para os exemplos.
- `estudo/assets/estilo.css` — só estrutura, copiado do ESTOCASTICOS e
  acrescido das classes de árvore para SVG: `.cx` (nó destacado), `.cx-folha`
  (nó neutro), `.ramo` (traço sem seta), `.tx`, `.tx-crit`. **Nunca escrever
  cor literal aqui.**

O `<head>` de toda página de aula:

```html
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>Cap. N — Título</title>
<link rel="stylesheet" href="../assets/tema.css?v=1">
<link rel="stylesheet" href="../assets/estilo.css?v=1">
```

Tudo o mais (grade de quebra de coluna, `.topo + .objetivo`, barra lateral
fixa com `<details class="sub">`, `h3` com `id="{h2}-{k}"`, `td.txt`,
`?v=` a incrementar ao mexer no CSS) é idêntico ao MULTI/ESTOCASTICOS.

**MathML — armadilhas já encontradas:**

- Espaço nas bordas de `<mtext>` é descartado. Use `<mspace width="0.35em"/>`
  fora do `<mtext>`.
- `<mfrac linethickness="0">` para coeficientes binomiais.
- **Equações em bloco com mais de ~700 px estouram a coluna de leitura** (46rem)
  e viram rolagem horizontal. Regra: no máximo duas igualdades por
  `<math display="block">`; a cadeia longa da demonstração de (2.15) foi
  partida em dois blocos. Conferir com JS no preview:
  `[...document.querySelectorAll('math[display=block]')].filter(m => m.scrollWidth > m.clientWidth + 1)`.
- Um `Write` só não cabe: cada aula tem 640–860 linhas. Escrever em três partes
  no scratchpad e concatenar com `cat`; validar o aninhamento com o
  `valida.py` (html.parser) a cada passada. **Heredocs no Bash quebram com
  conteúdo HTML longo** (aspas/contra-barras): usar o `Write` para os HTML.

## Preview local

O painel de navegador do Claude Code serve `file://` como snapshot (`data:`) e
não carrega o CSS relativo. Use `.claude/launch.json` (fora do git), que sobe
`python -m http.server 8765`, e abra
`http://localhost:8765/estudo/cap02/02-00-definicoes-e-notacoes-basicas.html`.
As capturas de tela falham depois de rolar a página (janela oculta); para
inspecionar os SVG, serializar com estilos computados e desenhar num canvas
via `javascript_tool`, salvando o PNG no scratchpad.

## Estrutura

```
AMOSTRAGEM/
├── elementos-de-amostragem.pdf   (fora do git: .gitignore)
├── index.html              redireciona para estudo/ — serve ao GitHub Pages
├── README.md               documentação pública do repositório
├── CLAUDE.md               este arquivo
├── .gitignore  .gitattributes  robots.txt
├── ferramentas/
│   ├── extrair.py
│   └── figuras.py
└── estudo/
    ├── index.html          painel com o percurso
    ├── assets/
    │   ├── tema.css        cores, fontes, medidas (azul-cobalto)
    │   └── estilo.css      estrutura e layout
    ├── cap01/
    │   ├── 01-00-nocoes-basicas.html
    │   └── img/fig-01-01.png
    ├── cap02/
    │   └── 02-00-definicoes-e-notacoes-basicas.html
    ├── cap03/
    │   └── 03-00-amostragem-aleatoria-simples.html
    └── cap04/
        └── 04-00-amostragem-estratificada.html   (diagrama SVG da população do Ex. 4.1)
```

O repositório está em <https://github.com/GABELCHIOR/AMOSTRAGEM> (remoto
`origin`, branch `main`). O PDF fica de fora pelo `.gitignore`. Para o GitHub
Pages servir o site, ativar em Settings → Pages → branch `main`, pasta `/`
(raiz); a `index.html` da raiz redireciona para `estudo/`.

## Progresso

**Capítulos 1 a 4 prontos** (caps. 1–2 em 2026-09-11; caps. 3–4 em
2026-09-21). Próximo: capítulo 5 (Estimadores do tipo razão, livro 127–144,
PDF 139–156). Ao gerar, retomar: a leitura "parte não observada" do estimador
expansão (cap. 3, seção 2.2); o Ex. 3.7 dos dentistas como razão com X
conhecido; a Tabela 2.8 (ρ_XY = 0,96, R = 0,682) é a população natural para
comparar razão × expansão; Tabela 5.1 do livro enumera `S_AASc` como o cap. 3
— refazer com `expand.grid`. O cap. 6 (regressão) segue o mesmo molde.
