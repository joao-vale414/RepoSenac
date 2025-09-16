CREATE DATABASE CARAMELO;

USE CARAMELO;

CREATE TABLE VENDA (
DATA_VENDA DATE, 
PRODUTO VARCHAR (100),
CATEGORIA VARCHAR(100),
VALOR_UNITARIO DECIMAL(10,2),
QUANTIDADE INT,
CLIENTE VARCHAR(100),
CIDADE VARCHAR(100),
ESTADOR VARCHAR(2) );

SELECT * FROM VENDA;

INSERT INTO VENDA (
DATA_VENDA,PRODUTO,CATEGORIA,VALOR_UNITARIO,QUANTIDADE,
CLIENTE,CIDADE,ESTADOR)
VALUES
('2024-12-30', 'Teclado', 'Acessórios', 1069.31, 7, 'Carlos', 'Porto Alegre', 'RS'),
('2025-05-29', 'Impressora', 'Acessórios', 3075.52, 6, 'Juliana', 'Fortaleza', 'CE'),
('2024-10-21', 'Teclado', 'Informática', 3471.0, 9, 'Fernanda', 'Recife', 'PE'),
('2024-12-20', 'Tablet', 'Eletrônicos', 778.08, 8, 'Lucas', 'Salvador', 'BA'),
('2025-04-06', 'Impressora', 'Eletrônicos', 527.14, 6, 'Pedro', 'Recife', 'PE'),
('2024-11-17', 'Smartphone', 'Informática', 4905.19, 2, 'Juliana', 'Rio de Janeiro', 'RJ'),
('2025-03-07', 'Mouse', 'Acessórios', 4123.17, 6, 'Pedro', 'São Paulo', 'SP'),
('2025-05-27', 'Smartphone', 'Acessórios', 3046.77, 9, 'Ana', 'Rio de Janeiro', 'RJ'),
('2025-01-26', 'Impressora', 'Eletrônicos', 80.37, 8, 'Maria', 'Salvador', 'BA'),
('2025-02-21', 'Tablet', 'Informática', 64.6, 5, 'Pedro', 'Rio de Janeiro', 'RJ'),
('2024-10-07', 'Impressora', 'Eletrônicos', 2201.78, 8, 'Juliana', 'Recife', 'PE'),
('2025-01-20', 'Tablet', 'Informática', 528.17, 3, 'Juliana', 'Rio de Janeiro', 'RJ'),
('2025-05-21', 'Mouse', 'Eletrônicos', 3658.58, 8, 'Pedro', 'Recife', 'PE'),
('2025-01-25', 'Mouse', 'Informática', 2679.83, 6, 'Carlos', 'Salvador', 'BA'),
('2025-07-29', 'Teclado', 'Eletrônicos', 1439.93, 9, 'Ana', 'Porto Alegre', 'RS'),
('2025-01-12', 'Fone de Ouvido', 'Informática', 2310.63, 9, 'Lucas', 'Curitiba', 'PR'),
('2024-12-10', 'Smartphone', 'Eletrônicos', 2000.74, 7, 'Juliana', 'Curitiba', 'PR'),
('2025-05-27', 'Monitor', 'Eletrônicos', 1888.07, 8, 'Carlos', 'Recife', 'PE'),
('2024-12-14', 'Impressora', 'Eletrônicos', 973.88, 8, 'Ana', 'Porto Alegre', 'RS'),
('2024-10-10', 'Tablet', 'Acessórios', 3941.24, 10, 'Ana', 'São Paulo', 'SP'),
('2024-11-06', 'Teclado', 'Informática', 2496.78, 10, 'João', 'Porto Alegre', 'RS'),
('2025-04-05', 'Smartphone', 'Acessórios', 1995.73, 1, 'Maria', 'Belo Horizonte', 'MG'),
('2024-11-02', 'Tablet', 'Acessórios', 449.95, 6, 'Ana', 'Recife', 'PE'),
('2025-02-18', 'Mouse', 'Acessórios', 2574.21, 5, 'Lucas', 'Salvador', 'BA'),
('2024-10-23', 'Teclado', 'Acessórios', 1232.54, 5, 'Ana', 'Salvador', 'BA'),
('2025-05-15', 'Notebook', 'Informática', 3906.87, 5, 'João', 'Curitiba', 'PR'),
('2025-04-01', 'Tablet', 'Informática', 3250.97, 8, 'João', 'Rio de Janeiro', 'RJ'),
('2025-08-03', 'Fone de Ouvido', 'Informática', 3541.49, 7, 'Ana', 'Belo Horizonte', 'MG'),
('2024-10-19', 'Tablet', 'Informática', 2065.88, 8, 'Pedro', 'Recife', 'PE'),
('2025-08-07', 'Impressora', 'Informática', 2647.94, 1, 'Fernanda', 'Rio de Janeiro', 'RJ'),
('2025-02-06', 'Tablet', 'Eletrônicos', 2072.84, 6, 'Juliana', 'Curitiba', 'PR'),
('2025-06-01', 'Notebook', 'Eletrônicos', 2139.95, 4, 'Juliana', 'Recife', 'PE'),
('2025-03-29', 'Mouse', 'Acessórios', 4541.91, 2, 'Fernanda', 'São Paulo', 'SP'),
('2025-01-11', 'Notebook', 'Eletrônicos', 2236.4, 1, 'Carlos', 'Recife', 'PE'),
('2024-12-05', 'Monitor', 'Eletrônicos', 2237.52, 10, 'Ana', 'Porto Alegre', 'RS'),
('2025-09-10', 'Monitor', 'Informática', 4452.22, 1, 'Maria', 'Fortaleza', 'CE'),
('2025-01-11', 'Impressora', 'Eletrônicos', 1899.3, 1, 'Carlos', 'Belo Horizonte', 'MG'),
('2025-03-03', 'Smartphone', 'Informática', 1827.33, 2, 'Carlos', 'Fortaleza', 'CE'),
('2025-09-11', 'Impressora', 'Eletrônicos', 2841.71, 10, 'Fernanda', 'Belo Horizonte', 'MG'),
('2025-01-06', 'Tablet', 'Eletrônicos', 352.52, 7, 'Juliana', 'Belo Horizonte', 'MG'),
('2025-03-28', 'Tablet', 'Eletrônicos', 2312.87, 10, 'Juliana', 'Fortaleza', 'CE'),
('2024-11-16', 'Fone de Ouvido', 'Acessórios', 526.51, 6, 'Pedro', 'Porto Alegre', 'RS'),
('2025-04-04', 'Smartphone', 'Acessórios', 4413.3, 2, 'Juliana', 'Curitiba', 'PR'),
('2025-01-08', 'Monitor', 'Informática', 2308.17, 2, 'Lucas', 'Recife', 'PE'),
('2025-04-13', 'Tablet', 'Eletrônicos', 2182.46, 10, 'Pedro', 'Fortaleza', 'CE'),
('2025-09-10', 'Monitor', 'Informática', 4956.39, 8, 'Lucas', 'Curitiba', 'PR'),
('2024-11-10', 'Mouse', 'Acessórios', 277.88, 4, 'Juliana', 'Curitiba', 'PR'),
('2025-05-31', 'Notebook', 'Acessórios', 1337.22, 5, 'Pedro', 'São Paulo', 'SP'),
('2024-12-09', 'Fone de Ouvido', 'Acessórios', 2292.84, 5, 'João', 'Salvador', 'BA'),
('2025-04-06', 'Teclado', 'Acessórios', 2088.29, 1, 'João', 'Porto Alegre', 'RS'),
('2025-04-16', 'Notebook', 'Eletrônicos', 501.28, 10, 'Ana', 'Recife', 'PE'),
('2025-02-08', 'Teclado', 'Informática', 1138.15, 1, 'Carlos', 'Salvador', 'BA'),
('2025-03-02', 'Notebook', 'Informática', 962.84, 9, 'Fernanda', 'Rio de Janeiro', 'RJ'),
('2025-07-18', 'Impressora', 'Eletrônicos', 2941.71, 6, 'Carlos', 'Recife', 'PE'),
('2025-04-25', 'Tablet', 'Eletrônicos', 4212.95, 9, 'Juliana', 'Porto Alegre', 'RS'),
('2025-02-27', 'Smartphone', 'Eletrônicos', 631.68, 5, 'Lucas', 'Salvador', 'BA'),
('2025-07-25', 'Mouse', 'Eletrônicos', 3909.02, 10, 'João', 'Belo Horizonte', 'MG'),
('2024-12-09', 'Notebook', 'Informática', 1936.83, 1, 'João', 'Salvador', 'BA'),
('2025-03-10', 'Monitor', 'Eletrônicos', 666.39, 5, 'Juliana', 'Recife', 'PE'),
('2025-04-21', 'Tablet', 'Informática', 1677.97, 10, 'Carlos', 'Salvador', 'BA'),
('2024-10-18', 'Notebook', 'Informática', 4954.81, 3, 'Fernanda', 'Belo Horizonte', 'MG'),
('2025-06-19', 'Impressora', 'Eletrônicos', 2276.96, 4, 'Carlos', 'Rio de Janeiro', 'RJ'),
('2025-03-05', 'Tablet', 'Informática', 4886.25, 10, 'Pedro', 'Belo Horizonte', 'MG'),
('2025-03-04', 'Notebook', 'Informática', 2436.69, 8, 'Lucas', 'Curitiba', 'PR'),
('2025-09-01', 'Impressora', 'Eletrônicos', 1158.88, 10, 'Maria', 'Recife', 'PE'),
('2025-08-15', 'Impressora', 'Informática', 4234.1, 9, 'João', 'São Paulo', 'SP'),
('2025-03-26', 'Notebook', 'Eletrônicos', 874.56, 9, 'Carlos', 'Fortaleza', 'CE'),
('2025-02-02', 'Smartphone', 'Acessórios', 1468.61, 3, 'Juliana', 'Recife', 'PE'),
('2025-06-11', 'Tablet', 'Acessórios', 2394.45, 4, 'Fernanda', 'Belo Horizonte', 'MG'),
('2025-05-11', 'Teclado', 'Eletrônicos', 1503.44, 9, 'Juliana', 'Rio de Janeiro', 'RJ'),
('2025-07-28', 'Teclado', 'Acessórios', 505.92, 5, 'Maria', 'Porto Alegre', 'RS'),
('2025-08-20', 'Monitor', 'Eletrônicos', 1841.19, 7, 'Juliana', 'Salvador', 'BA'),
('2025-03-31', 'Mouse', 'Eletrônicos', 1618.75, 10, 'João', 'Rio de Janeiro', 'RJ'),
('2025-08-10', 'Mouse', 'Eletrônicos', 2501.81, 5, 'Carlos', 'Recife', 'PE'),
('2025-03-06', 'Monitor', 'Eletrônicos', 4531.06, 6, 'Pedro', 'Belo Horizonte', 'MG'),
('2024-11-29', 'Tablet', 'Acessórios', 1064.74, 1, 'Fernanda', 'Porto Alegre', 'RS'),
('2024-12-27', 'Fone de Ouvido', 'Acessórios', 4621.67, 8, 'Juliana', 'São Paulo', 'SP'),
('2025-03-07', 'Smartphone', 'Acessórios', 477.01, 2, 'Lucas', 'Porto Alegre', 'RS'),
('2025-02-23', 'Mouse', 'Informática', 811.58, 6, 'Carlos', 'São Paulo', 'SP'),
('2025-07-02', 'Mouse', 'Acessórios', 4514.64, 3, 'Carlos', 'Fortaleza', 'CE'),
('2024-10-18', 'Mouse', 'Informática', 1604.42, 9, 'Fernanda', 'Recife', 'PE'),
('2024-09-26', 'Mouse', 'Acessórios', 4714.85, 2, 'Carlos', 'Curitiba', 'PR'),
('2024-12-02', 'Teclado', 'Informática', 4648.69, 10, 'Ana', 'Porto Alegre', 'RS'),
('2025-01-03', 'Mouse', 'Eletrônicos', 3367.1, 5, 'Maria', 'São Paulo', 'SP'),
('2025-07-29', 'Impressora', 'Informática', 1308.0, 10, 'Pedro', 'Belo Horizonte', 'MG'),
('2024-09-23', 'Monitor', 'Informática', 3075.7, 2, 'Carlos', 'Curitiba', 'PR'),
('2025-06-20', 'Fone de Ouvido', 'Informática', 909.6, 3, 'Lucas', 'Salvador', 'BA'),
('2025-04-16', 'Mouse', 'Acessórios', 3577.64, 4, 'Lucas', 'Curitiba', 'PR'),
('2024-09-22', 'Notebook', 'Acessórios', 3430.6, 3, 'Carlos', 'Curitiba', 'PR'),
('2024-12-30', 'Notebook', 'Informática', 2818.95, 1, 'Lucas', 'Recife', 'PE'),
('2024-09-20', 'Impressora', 'Acessórios', 599.73, 4, 'Maria', 'São Paulo', 'SP'),
('2025-05-13', 'Mouse', 'Eletrônicos', 1024.53, 3, 'Carlos', 'Curitiba', 'PR'),
('2025-05-17', 'Teclado', 'Informática', 1375.5, 6, 'Fernanda', 'Porto Alegre', 'RS'),
('2025-01-25', 'Teclado', 'Acessórios', 4485.75, 4, 'Maria', 'São Paulo', 'SP'),
('2025-05-27', 'Impressora', 'Informática', 826.32, 10, 'Carlos', 'Belo Horizonte', 'MG'),
('2025-07-16', 'Teclado', 'Acessórios', 4921.07, 5, 'Fernanda', 'Salvador', 'BA'),
('2024-09-23', 'Monitor', 'Informática', 4000.48, 4, 'Lucas', 'Recife', 'PE'),
('2025-08-04', 'Monitor', 'Informática', 326.44, 9, 'Ana', 'Curitiba', 'PR'),
('2024-10-30', 'Tablet', 'Eletrônicos', 3788.94, 9, 'Fernanda', 'Belo Horizonte', 'MG'),
('2024-10-11', 'Monitor', 'Informática', 407.14, 10, 'Maria', 'São Paulo', 'SP'),
('2024-09-28', 'Notebook', 'Informática', 3957.08, 6, 'Juliana', 'São Paulo', 'SP'),
('2025-05-26', 'Impressora', 'Eletrônicos', 450.16, 4, 'Pedro', 'Fortaleza', 'CE'),
('2025-06-12', 'Notebook', 'Informática', 4564.6, 3, 'Maria', 'São Paulo', 'SP'),
('2024-10-24', 'Smartphone', 'Informática', 1304.2, 2, 'Carlos', 'Curitiba', 'PR'),
('2024-12-27', 'Fone de Ouvido', 'Informática', 707.91, 4, 'Ana', 'Salvador', 'BA'),
('2025-06-24', 'Mouse', 'Eletrônicos', 4581.03, 2, 'Maria', 'Curitiba', 'PR'),
('2025-02-23', 'Mouse', 'Acessórios', 715.96, 2, 'Juliana', 'Porto Alegre', 'RS'),
('2025-08-17', 'Notebook', 'Eletrônicos', 2751.9, 10, 'Pedro', 'Belo Horizonte', 'MG'),
('2025-06-28', 'Mouse', 'Eletrônicos', 4530.58, 7, 'Juliana', 'Fortaleza', 'CE'),
('2025-01-06', 'Notebook', 'Eletrônicos', 247.06, 10, 'Pedro', 'Belo Horizonte', 'MG'),
('2024-10-03', 'Teclado', 'Acessórios', 2180.13, 8, 'Lucas', 'São Paulo', 'SP'),
('2025-02-23', 'Tablet', 'Eletrônicos', 2775.68, 3, 'Maria', 'Fortaleza', 'CE'),
('2024-10-31', 'Monitor', 'Eletrônicos', 2655.55, 2, 'Maria', 'Belo Horizonte', 'MG'),
('2025-04-09', 'Fone de Ouvido', 'Acessórios', 2418.81, 2, 'Juliana', 'Porto Alegre', 'RS'),
('2025-07-12', 'Teclado', 'Eletrônicos', 4037.04, 9, 'Carlos', 'Belo Horizonte', 'MG'),
('2025-04-15', 'Notebook', 'Eletrônicos', 4782.34, 3, 'Pedro', 'Recife', 'PE'),
('2024-10-02', 'Fone de Ouvido', 'Acessórios', 3320.8, 7, 'Maria', 'Recife', 'PE'),
('2025-06-08', 'Monitor', 'Informática', 1261.08, 1, 'Ana', 'Porto Alegre', 'RS'),
('2024-10-07', 'Smartphone', 'Informática', 691.4, 9, 'João', 'Rio de Janeiro', 'RJ'),
('2025-02-23', 'Smartphone', 'Informática', 4609.05, 3, 'João', 'Salvador', 'BA'),
('2025-09-01', 'Smartphone', 'Acessórios', 3033.4, 2, 'Maria', 'Belo Horizonte', 'MG'),
('2025-02-19', 'Monitor', 'Informática', 1631.07, 7, 'Juliana', 'Porto Alegre', 'RS'),
('2025-06-06', 'Teclado', 'Eletrônicos', 1440.27, 1, 'Ana', 'São Paulo', 'SP'),
('2024-09-21', 'Mouse', 'Informática', 590.56, 1, 'Ana', 'Porto Alegre', 'RS'),
('2025-05-14', 'Notebook', 'Eletrônicos', 4062.68, 4, 'Fernanda', 'Salvador', 'BA'),
('2024-12-27', 'Smartphone', 'Acessórios', 4250.31, 2, 'Pedro', 'Porto Alegre', 'RS'),
('2025-04-26', 'Fone de Ouvido', 'Acessórios', 3281.37, 9, 'Ana', 'Belo Horizonte', 'MG'),
('2025-02-11', 'Smartphone', 'Eletrônicos', 4369.86, 10, 'Pedro', 'Curitiba', 'PR'),
('2025-04-03', 'Tablet', 'Acessórios', 100.45, 8, 'Maria', 'Porto Alegre', 'RS'),
('2025-06-19', 'Fone de Ouvido', 'Eletrônicos', 2472.99, 9, 'Ana', 'Recife', 'PE'),
('2025-06-21', 'Mouse', 'Informática', 2655.65, 8, 'Ana', 'Fortaleza', 'CE'),
('2024-11-14', 'Teclado', 'Eletrônicos', 284.59, 9, 'João', 'Belo Horizonte', 'MG'),
('2025-05-14', 'Mouse', 'Informática', 1713.47, 3, 'Ana', 'Recife', 'PE'),
('2025-06-21', 'Mouse', 'Informática', 2964.64, 7, 'João', 'Recife', 'PE'),
('2024-12-08', 'Teclado', 'Acessórios', 572.86, 5, 'Ana', 'Belo Horizonte', 'MG'),
('2025-06-03', 'Monitor', 'Acessórios', 1115.85, 10, 'Fernanda', 'Belo Horizonte', 'MG'),
('2024-10-13', 'Fone de Ouvido', 'Informática', 4890.0, 6, 'Fernanda', 'Recife', 'PE'),
('2024-10-19', 'Fone de Ouvido', 'Informática', 3127.68, 10, 'Lucas', 'Fortaleza', 'CE'),
('2025-09-08', 'Monitor', 'Eletrônicos', 2202.63, 3, 'Lucas', 'Fortaleza', 'CE'),
('2025-08-14', 'Notebook', 'Acessórios', 3512.49, 10, 'Fernanda', 'Porto Alegre', 'RS'),
('2024-12-24', 'Impressora', 'Eletrônicos', 3605.48, 7, 'Juliana', 'Fortaleza', 'CE'),
('2024-11-08', 'Tablet', 'Informática', 1950.54, 8, 'Carlos', 'Belo Horizonte', 'MG'),
('2025-06-14', 'Smartphone', 'Acessórios', 2224.58, 10, 'Carlos', 'Belo Horizonte', 'MG'),
('2025-03-21', 'Mouse', 'Informática', 603.95, 5, 'Fernanda', 'Recife', 'PE'),
('2024-10-19', 'Monitor', 'Acessórios', 3696.99, 2, 'Juliana', 'Salvador', 'BA'),
('2025-05-22', 'Tablet', 'Informática', 529.56, 7, 'Fernanda', 'Fortaleza', 'CE'),
('2024-11-26', 'Teclado', 'Informática', 2449.32, 2, 'Fernanda', 'São Paulo', 'SP'),
('2025-04-03', 'Notebook', 'Acessórios', 1273.36, 3, 'Fernanda', 'São Paulo', 'SP'),
('2025-08-17', 'Notebook', 'Eletrônicos', 3413.49, 6, 'Maria', 'Belo Horizonte', 'MG'),
('2024-10-09', 'Smartphone', 'Informática', 1278.15, 3, 'João', 'Rio de Janeiro', 'RJ');

SELECT PRODUTO,CATEGORIA,VALOR_UNITARIO FROM VENDA;

SELECT PRODUTO,CATEGORIA,VALOR_UNITARIO
FROM VENDA
WHERE CATEGORIA = "Informática";

SELECT CLIENTE,DATA_VENDA,ESTADOR
FROM VENDA
WHERE VALOR_UNITARIO > 1000;

SELECT PRODUTO,VALOR_UNITARIO
FROM VENDA
ORDER BY VALOR_UNITARIO DESC;

SELECT SUM(QUANTIDADE * VALOR_UNITARIO) AS VALOR_VENDIDO
FROM VENDA;

SELECT ESTADOR, COUNT(*) AS QUANTIDADE_VENDA_ESTADO
FROM VENDA 
GROUP BY ESTADOR;

SELECT ESTADOR, SUM(QUANTIDADE * VALOR_UNITARIO) AS VALOR_VENDIDO
FROM VENDA
GROUP BY ESTADOR;

SELECT CLIENTE,
SUM(VALOR_UNITARIO * QUANTIDADE) AS TOTAL_CLIENTE
FROM VENDA
WHERE CATEGORIA = "Informática"
GROUP BY CLIENTE
HAVING TOTAL_CLIENTE > 5000 AND TOTAL_CLIENTE < 50000;

SELECT CATEGORIA,
AVG(VALOR_UNITARIO * QUANTIDADE) AS MEDIA_VENDIDA
FROM VENDA
GROUP BY CATEGORIA;

