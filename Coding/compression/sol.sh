for i in {2500..1..-1}
do
    echo $i
    if [[ -e flag$i.tar.gz ]]; then
        gunzip flag$i.tar.gz
        tar xvf flag$i.tar
    elif [[ -e flag$i.tar ]]; then
        tar xvf flag$i.tar
    elif [[ -e flag$i.tar.xz ]]; then
        tar xvf flag$i.tar.xz
    elif [[ -e flag$i.tar.bz2 ]]; then
        bzip2 -d flag$i.tar.bz2
        tar xvf flag$i.tar
    else
        exit
    fi
done
