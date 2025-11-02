# Instruções para Subir o Projeto no GitHub

## Opção 1: Criar repositório manualmente no GitHub

1. **Acesse o GitHub** (https://github.com) e faça login
2. **Clique em "New repository"** (novo repositório)
3. **Configure o repositório:**
   - Nome: `home-hero-python` (ou outro nome de sua escolha)
   - Descrição: "Backend HomeHero convertido de Java para Python"
   - Escolha se será público ou privado
   - **NÃO** inicialize com README, .gitignore ou licença (já temos isso)
4. **Clique em "Create repository"**

5. **Execute os comandos abaixo no terminal:**

```powershell
cd c:\Users\matheus\Desktop\home-hero-python
git remote add origin https://github.com/SEU_USUARIO/home-hero-python.git
git branch -M main
git push -u origin main
```

**Substitua `SEU_USUARIO` pelo seu usuário do GitHub e ajuste o nome do repositório se necessário.**

## Opção 2: Usar GitHub CLI (se instalar)

Se preferir instalar o GitHub CLI (`gh`):

1. Instale o GitHub CLI: https://cli.github.com/
2. Execute:
```powershell
cd c:\Users\matheus\Desktop\home-hero-python
gh auth login
gh repo create home-hero-python --public --source=. --remote=origin --push
```

## Verificar o status

Após adicionar o remote e fazer push, você pode verificar com:

```powershell
git remote -v
git status
```

## Nota

O projeto já está commitado localmente. Você só precisa:
1. Criar o repositório no GitHub (web ou CLI)
2. Adicionar o remote
3. Fazer push

