def soma_lista(somados, a):
    if a==0:
        return 0
    return somados(a) + somados(a-1)


int main():