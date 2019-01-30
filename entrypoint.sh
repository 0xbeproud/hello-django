#!/usr/bin/env bash

export ENV_SECRETS_DIR=/run/secrets

for file in ${ENV_SECRETS_DIR}/*; do
    [ -f "$file" ] || continue
    # non_export로 시작하는 docker secret 파일은 환경변수로 로딩하지 않는다..
    [[ $(basename $file) == non_export* ]] && continue

    name=$(echo $file | awk '{print toupper($0)}')
    name=${name##*/}
    export "$name"=$(cat "$file")
done

echo "python manage.py migrate"
python manage.py migrate
echo "python manage.py collectstatic --noinput"
python manage.py collectstatic --noinput

exec $@