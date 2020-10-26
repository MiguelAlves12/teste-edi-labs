### Teste Estagiário - Python

O teste deve ser realizado na linguagem de programação Python.

> Recomenda-se utilizar a versão 3 do Python.

Deve-se desenvolver dois scripts:

### 1) Script capaz de realizar a conversão de um arquivo JSON para um arquivo CSV, seguindo o exemplo a seguir:

```JSON
{
	"order": [
		{
			"id": 1,
			"name": "Boné",
			"description": "Boné Branco",
			"quantity": 2,
			"value": 25.20
		},
		{
			"id": 2,
			"name": "Camiseta",
			"description": "Camiseta 100% Algodão",
			"quantity": 3,
			"value": 18.50
		},
		{
			"id": 3,
			"name": "Calça",
			"description": "Calça Jeans",
			"quantity": 1,
			"value": 29.90
		}
	]
}
```

> Este arquivo pode ser encontrado no diretório ./json/exemplo/shopping.json

#### CSV Gerado

| ID  | Name | Description | Quantity | Value | Total |
| ------------- | ------------- | ------------- | ------------- | ------------- | -------------|
| 1  | Boné | Boné Branco | 2 | 25.2 | 50.4 |
| 2  | Camiseta | Camiseta 100% Algodão | 3 | 18.5 | 55.5 |
| 3  | Calça | Calça Jeans | 1 | 29.9 | 29.9 |
| Total  |  |  |  |  | 135.8 |

#### Requisitos

- [ ] O arquivo CSV deve ser criado com o separador Pipe (**|**)
- [ ] A coluna **Total** deve conter o valor total de cada produto levando em conta as suas quantidades.
- [ ] A linha **Total** deve conter o valor total do pedido.

# 

### 2) Script capaz de realizar a conversão de um arquivo CSV para um arquivo JSON, seguindo o exemplo a seguir:

#### CSV

ID  | Name | Description | Quantity | Value
------------- | ------------- | ------------- | ------------- | -------------
1  | Boné | Boné Branco | 2 | 25.2 
2  | Camiseta | Camiseta 100% Algodão | 3 | 18.5 
3  | Calça | Calça Jeans | 1 | 29.9 
> Este arquivo pode ser encontrado no diretório ./csv/exemplo/shopping.csv

#### JSON Gerado

```JSON
	{
	"order": [
		{
			"id": 1,
			"name": "Boné",
			"description": "Boné Branco",
			"quantity": 2,
			"value": 25.20
		},
		{
			"id": 2,
			"name": "Camiseta",
			"description": "Camiseta 100% Algodão",
			"quantity": 3,
			"value": 18.50
		},
		{
			"id": 3,
			"name": "Calça",
			"description": "Calça Jeans",
			"quantity": 1,
			"value": 29.90
		}
	],
	"total": 135.8
}
```

#### Requisitos

- [ ] A propriedade "total" no JSON gerado deve conter o valor total do pedido.

# 

Fique a vontade para clonar este repositório.

> Utilize os arquivos **./json/shopping.json** e **./csv/shopping.csv** para gerar os arquivos com seus respectivos scripts.

> Os arquivos devem ser gerados no diretório **./gerados/**

Quando terminar o desenvolvimento, envie o link do seu repositório para o e-mail ***cintia.andrade@edi-labs.com***.

# 
