# Sistema de Gerenciamento de Tarefas 📋

## 👨‍💻 Aluno(a)
[Seu Nome]

## 📝 Descrição do Projeto

Sistema web simples e funcional desenvolvido em **Django** para gerenciar tarefas com categorização. O sistema permite criar, consultar, editar e deletar tarefas, organizadas por categorias profissionais.

### Problema Resolvido
📌 Necessidade de um sistema para organizar e controlar tarefas do dia a dia com classificação por categorias, facilitando o acompanhamento de atividades profissionais.

### Público-Alvo
👥 Profissionais e equipes que precisam organizar suas atividades diárias de forma simples e eficiente.

---

## ✨ Funcionalidades Principais

✅ **Listar Tarefas** - Visualizar todas as tarefas cadastradas com seus detalhes  
✅ **Criar Tarefas** - Adicionar novas tarefas com título, descrição e categoria  
✅ **Editar Tarefas** - Modificar dados de tarefas existentes  
✅ **Deletar Tarefas** - Remover tarefas do sistema  
✅ **Categorizar Tarefas** - Organizar tarefas por categorias  
✅ **Tratamento de Erros** - Validação de dados e mensagens de erro/sucesso  
✅ **Interface Web** - Interface amigável e responsiva com Django  

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Descrição |
|-----------|-----------|
| **Python 3.x** | Linguagem de programação |
| **Django 6.0+** | Framework web |
| **SQLite** | Banco de dados |
| **HTML/CSS** | Interface web |
| **Git** | Versionamento de código |

---

## 📊 Requisitos Técnicos Atendidos

### Python ✅
- [x] Variáveis e entrada de dados
- [x] Estruturas condicionais
- [x] Laços de repetição
- [x] Funções
- [x] Tratamento de erros

### Programação Orientada a Objetos ✅
- [x] Classes (`Categoria`, `Tarefa`)
- [x] Atributos e métodos
- [x] Instanciação de objetos

### Banco de Dados ✅
- [x] SQLite (`db.sqlite3`)
- [x] 2 tabelas relacionadas (Categoria + Tarefa com ForeignKey)
- [x] CRUD completo implementado

### Interface ✅
- [x] Interface web com Django

### Versionamento ✅
- [x] Repositório no GitHub
- [x] Mínimo 5 commits

---

## 📁 Estrutura do Projeto

```
projeto/
├── manage.py                 # Arquivo principal Django
├── db.sqlite3               # Banco de dados
├── README.md                # Este arquivo
├── projeto/                 # Configurações do projeto
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py              # URLs principais
│   ├── asgi.py
│   └── wsgi.py
└── tarefas/                 # Aplicação principal
    ├── models.py            # Classes Categoria e Tarefa
    ├── views.py             # Lógica das funcionalidades
    ├── urls.py              # URLs da app
    ├── admin.py
    ├── apps.py
    ├── migrations/          # Migrações do banco
    └── templates/
        └── tarefas/
            ├── lista.html           # Listagem de tarefas
            ├── formulario.html      # Criar nova tarefa
            └── editar.html          # Editar tarefa existente
```

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
- Python 3.8+
- pip (gerenciador de pacotes Python)

### Passo a Passo

1. **Clone o repositório**
```bash
git clone https://github.com/seu-usuario/projeto-tarefas.git
cd projeto-tarefas
```

2. **Instale as dependências**
```bash
pip install django
```

3. **Configure o banco de dados** (se necessário)
```bash
cd projeto
python manage.py migrate
```

4. **Crie um usuário admin** (opcional)
```bash
python manage.py createsuperuser
```

5. **Inicie o servidor**
```bash
python manage.py runserver
```

6. **Acesse o sistema**
- Abra o navegador e digite: `http://127.0.0.1:8000/`
- Admin: `http://127.0.0.1:8000/admin/`

---

## 📸 Screenshots do Sistema

### 1. Página Principal - Listagem de Tarefas
![Listagem]  (adicionar screenshot aqui)

**Funcionalidades visíveis:**
- Lista de todas as tarefas
- Botão "Nova Tarefa"
- Links para Editar e Deletar

### 2. Criar Nova Tarefa
![Criar]  (adicionar screenshot aqui)

**Formulário com:**
- Campo Título
- Campo Descrição
- Seletor de Categoria
- Botão Salvar

### 3. Editar Tarefa
![Editar]  (adicionar screenshot aqui)

**Formulário de edição com:**
- Dados pré-preenchidos
- Opção de alterar categoria
- Validação de campos

---

## 🧠 Explicação do Tratamento de Erros

### O que é Tratamento de Erros?
É um mecanismo para capturar e tratar problemas que podem ocorrer durante a execução do programa, evitando que a aplicação quebre abruptamente.

### Estrutura Try-Except em Python

```python
try:
    # Código que pode gerar erro
    tarefa = Tarefa.objects.get(id=id)
except ObjectDoesNotExist:
    # Captura erro específico - Objeto não encontrado
    messages.error(request, 'Tarefa não encontrada!')
    return redirect('lista')
except Exception as e:
    # Captura qualquer outro erro
    messages.error(request, f'Erro: {str(e)}')
```

### Tipos de Erros Tratados no Projeto

#### 1️⃣ **ObjectDoesNotExist** - Tarefa/Categoria não encontrada
```python
try:
    tarefa = Tarefa.objects.get(id=id)
except ObjectDoesNotExist:
    messages.error(request, 'Tarefa não encontrada!')
    return redirect('lista')
```
**Quando ocorre:** Tentativa de editar/deletar uma tarefa com ID inexistente

#### 2️⃣ **Campos Vazios** - Validação de dados
```python
titulo = request.POST.get('titulo', '').strip()
if not titulo:
    messages.error(request, 'Título não pode estar vazio!')
```
**Quando ocorre:** Usuário tenta salvar tarefa sem preencher campos obrigatórios

#### 3️⃣ **Categoria Inválida** - Validação de seleção
```python
try:
    categoria = Categoria.objects.get(id=categoria_id)
except ObjectDoesNotExist:
    messages.error(request, 'Categoria selecionada não existe!')
```
**Quando ocorre:** Tentativa de usar uma categoria que foi deletada

#### 4️⃣ **Erros Genéricos** - Captura geral
```python
except Exception as e:
    messages.error(request, f'Erro ao criar tarefa: {str(e)}')
```
**Quando ocorre:** Qualquer outro erro não previsto

### Mensagens de Feedback ao Usuário
```python
messages.success(request, 'Tarefa criada com sucesso!')  # ✅ Sucesso
messages.error(request, 'Erro ao deletar tarefa!')       # ❌ Erro
```

---

## 🔧 Funções Principais e Tratamento

### 1. `lista_tarefas(request)` - Listar todas as tarefas
```python
def lista_tarefas(request):
    try:
        tarefas = Tarefa.objects.all()
        return render(request, 'tarefas/lista.html', {'tarefas': tarefas})
    except Exception as e:
        messages.error(request, f'Erro ao carregar tarefas: {str(e)}')
```

### 2. `nova_tarefa(request)` - Criar nova tarefa
```python
# Valida título
if not titulo:
    messages.error(request, 'Título não pode estar vazio!')
    
# Valida descrição
if not descricao:
    messages.error(request, 'Descrição não pode estar vazia!')
    
# Valida categoria existe
try:
    categoria = Categoria.objects.get(id=categoria_id)
except ObjectDoesNotExist:
    messages.error(request, 'Categoria selecionada não existe!')
```

### 3. `editar_tarefa(request, id)` - Editar tarefa
```python
try:
    tarefa = Tarefa.objects.get(id=id)
except ObjectDoesNotExist:
    messages.error(request, 'Tarefa não encontrada!')
    return redirect('lista')
```

### 4. `deletar_tarefa(request, id)` - Deletar tarefa
```python
try:
    tarefa = Tarefa.objects.get(id=id)
    tarefa_titulo = tarefa.titulo
    tarefa.delete()
    messages.success(request, f'Tarefa "{tarefa_titulo}" deletada!')
except ObjectDoesNotExist:
    messages.error(request, 'Tarefa não encontrada!')
```

---

## 🎯 Dificuldades Encontradas

1. **Estrutura de Templates** - Inicialmente, os templates estavam na pasta errada, causando erro `TemplateDoesNotExist`
   - ✅ Solução: Reorganizar em `tarefas/templates/tarefas/`

2. **Campo Categoria Obrigatório** - O modelo Tarefa tinha categoria como campo obrigatório, causando erro ao criar tarefas
   - ✅ Solução: Adicionar `null=True, blank=True` na ForeignKey

3. **Falta de Validação de Dados** - Sistema aceitava dados vazios
   - ✅ Solução: Implementar validação com `.strip()` e verificação de campos

4. **Ausência de Tratamento de Erros** - Erros causavam crash da aplicação
   - ✅ Solução: Adicionar try-except em todas as views

---

## 📚 Aprendizados Principais

1. **Django Framework** - Estrutura MVC (Model-View-Controller) e funcionamento de apps
2. **Banco de Dados Relacional** - Uso de ForeignKey e relacionamentos entre tabelas
3. **Tratamento de Exceções** - Importância de capturar erros para melhor UX
4. **Validação de Dados** - Necessidade de validar entrada do usuário
5. **Mensagens de Feedback** - Sistema de messages do Django para comunicação com usuário
6. **Git e Versionamento** - Boas práticas de commit e organização do código

---

## 📋 Checklist de Entrega

- [x] Código funcionando completamente
- [x] Banco de dados com 2+ tabelas
- [x] CRUD implementado
- [x] Tratamento de erros robusto
- [x] Interface web com Django
- [x] README.md completo
- [x] Estrutura organizada de pastas
- [x] Mínimo 5 commits no Git
- [ ] Screenshots de funcionamento
- [ ] Apresentação em PDF/Slides
- [ ] Vídeo demonstrativo (opcional)

---

## 📞 Contato

Para dúvidas ou sugestões sobre o projeto, entre em contato através do GitHub.

---

**Data de Criação:** 18 de Março de 2026  
**Versão:** 1.0  
**Status:** ✅ Concluído
