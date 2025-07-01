🗺️ Mapa de Desenvolvimento do Projeto suSH
🧱 Fase 1: Estrutura Inicial

✅ Objetivo: Criar a base do projeto e organizar o ambiente

Criar estrutura de diretórios e arquivos principais (src/, commands/, shell.py, main.py, etc)

Escrever o README.md com visão geral

Criar ambiente virtual e requirements.txt

Escrever setup.py com entry point (sush)

    Iniciar controle de versão com Git

💬 Fase 2: Terminal Interativo

✅ Objetivo: Criar um shell funcional com prompt, histórico e parsing

Usar prompt_toolkit para criar um prompt customizado (suSH >)

Habilitar histórico (em memória e em arquivo .sush_history)

Adicionar autocompletar básico com comandos internos (help, exit, etc)

Tratar sinais (Ctrl+C, Ctrl+D) de forma elegante

    Criar roteador de comandos (handle_input())

⚙️ Fase 3: Núcleo de Comandos

✅ Objetivo: Organizar os comandos de forma modular e funcional

Criar pasta commands/

Criar interface comum ou classe base opcional para comandos

Implementar comandos básicos:

help — mostra lista de comandos

exit — encerra o shell

rf — remove arquivo (forçado)

    rnf — remove arquivo se existir (sem erro)

Adicionar comandos de sistema:

cd

ls

        Outros opcionais (cat, touch, etc)

🔧 Fase 4: Utilitários e Funcionalidades Extras

✅ Objetivo: Melhorar usabilidade, desempenho e organização

Criar utils.py para funções auxiliares (ex: validar caminho, formatar erro)

Adicionar logs de erro/eventos

Adicionar arquivo de configuração opcional (config.json)

    Criar testes unitários básicos com pytest

🔐 Fase 5: Segurança e Plugins (Avançado)

✅ Objetivo: Tornar o projeto mais robusto e expansível

Criar suporte a plugins externos (módulos que viram comandos)

Adicionar comandos de criptografia (usando cryptography)

Adicionar verificação de permissões antes de executar comandos sensíveis

    Suporte a alias ou variáveis no shell (set VAR=VALOR)

🚀 Fase 6: Empacotamento e Execução

✅ Objetivo: Transformar suSH em um programa utilizável

Finalizar setup.py com entry_points para comando sush

Criar executável com pyinstaller (opcional)

Adicionar ícone e nome no terminal (estilo fish/bash)

Publicar no GitHub com README completo

    Testar instalação com pip install .

🧪 Fase 7: Testes e Polimento

✅ Objetivo: Garantir estabilidade e boa experiência

Criar testes para comandos (test_commands/)

Testar prompt_toolkit em múltiplos SOs (Linux, Windows, WSL)

Corrigir bugs e inconsistências

Atualizar documentação final (ex: lista de comandos suportados)