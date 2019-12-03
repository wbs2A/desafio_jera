# desafio_jera
Esse repositório criado para armazenar os arquivos do desafio prático da Jera
----
### Considerações sobre a implementação
- O cadastro pode ser feito na aba sign up/login, o sistema de Social Auth não está funcionando devidamente.
 - Ao adicionar um filme na lista, um evento será lançado e quando o filme tiver sido inserido a página dará um refresh voltando para o início (após isso, o filme já está disponível para ser acessado na lista).
 - Ao criar uma conta, é necessário ir no painel para incluir um (ou mais perfis), mas após inseridos os perfis é possível selecionar um para ser utilizado na sessão, onde cada perfil armazena sua própria lista de filmes para assistir.
 - Para acrescentar um filme à lista é necessário selecionar um perfil antes.
 - A página ainda não trabalha com cookies ou implementações possíveis para sugestão de títulos.
- Os filmes populares são exibidos já de início na página e pode-se obter detalhes clicando no título de escolha.
### Instruções de uso
- Ao clicar na imagem de um filme pode-se obter detalhes dele (logado ou não, seja na página principal ou a partir da busca)
- Para fazer as ações que necessitam de acesso (como ver a lista de filmes selecionadas) deve ser feito o cadastro/login.
- Após feito o login (ou terminado o cadastro) deve-se ir em "Perfis e Config."  e inserir um novo perfil.
- Após inserido um novo perfil (ou mais), deve-se escolher o perfil da sessão, clicando na imagem associada.
- Agora é possível visualizar a lista de filmes ou inserir novos filmes à lista.
