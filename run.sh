#!/bin/sh
set -e  # Interrompe o script se houver erro

# Path para os dados de soluções dos alunos
TARGET_PATH="${PWD}/ui"
FUNCTION_NAME="posLetra"

# Helper para chamar a versão certa do Python
PYTHON="pipenv run python"

PYTHON_VERSION=$($PYTHON --version)
echo "Running with: $PYTHON_VERSION"

# Verifica se foi passada a flag '-a', indicando que apenas a análise deve ser feita
while getopts 'a' OPTION; do
    case "$OPTION" in
        a) 
            # Executa a análise das soluções
            $PYTHON src/run_pipeline.py $TARGET_PATH --run-pipeline -d
            ;;
    esac
done

# Se nao foram passadas flags, executa o pipeline completo
if (( $OPTIND == 1 ));
then
    # Executa as soluções dos alunos
    $PYTHON src/run_pipeline.py $TARGET_PATH --run-pre -n $FUNCTION_NAME
    # Executa a análise das soluções
    $PYTHON src/run_pipeline.py $TARGET_PATH --run-pipeline -d
fi

# Roda o servidor da interface
cd ./ui
./runServer.sh
