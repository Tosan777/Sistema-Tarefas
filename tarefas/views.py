from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from .models import Tarefa, Categoria


def lista_tarefas(request):
    try:
        tarefas = Tarefa.objects.all()
        return render(request, 'tarefas/lista.html', {'tarefas': tarefas})
    except Exception as e:
        messages.error(request, f'Erro ao carregar tarefas: {str(e)}')
        return render(request, 'tarefas/lista.html', {'tarefas': []})


def nova_tarefa(request):
    try:
        categorias = Categoria.objects.all()

        if request.method == 'POST':
            titulo = request.POST.get('titulo', '').strip()
            descricao = request.POST.get('descricao', '').strip()
            categoria_id = request.POST.get('categoria')

            if not titulo:
                messages.error(request, 'Título não pode estar vazio!')
                return render(request, 'tarefas/formulario.html', {'categorias': categorias})

            if not descricao:
                messages.error(request, 'Descrição não pode estar vazia!')
                return render(request, 'tarefas/formulario.html', {'categorias': categorias})

            if not categoria_id:
                messages.error(request, 'Selecione uma categoria!')
                return render(request, 'tarefas/formulario.html', {'categorias': categorias})

            try:
                categoria = Categoria.objects.get(id=categoria_id)
            except ObjectDoesNotExist:
                messages.error(request, 'Categoria selecionada não existe!')
                return render(request, 'tarefas/formulario.html', {'categorias': categorias})

            Tarefa.objects.create(
                titulo=titulo,
                descricao=descricao,
                categoria=categoria
            )
            messages.success(request, 'Tarefa criada com sucesso!')
            return redirect('lista')

        return render(request, 'tarefas/formulario.html', {'categorias': categorias})
    except Exception as e:
        messages.error(request, f'Erro ao criar tarefa: {str(e)}')
        return render(request, 'tarefas/formulario.html', {'categorias': []})


def editar_tarefa(request, id):
    try:
        tarefa = Tarefa.objects.get(id=id)
        categorias = Categoria.objects.all()

        if request.method == 'POST':
            titulo = request.POST.get('titulo', '').strip()
            descricao = request.POST.get('descricao', '').strip()
            categoria_id = request.POST.get('categoria')

            if not titulo:
                messages.error(request, 'Título não pode estar vazio!')
                return render(request, 'tarefas/editar.html', {'tarefa': tarefa, 'categorias': categorias})

            if not descricao:
                messages.error(request, 'Descrição não pode estar vazia!')
                return render(request, 'tarefas/editar.html', {'tarefa': tarefa, 'categorias': categorias})

            if not categoria_id:
                messages.error(request, 'Selecione uma categoria!')
                return render(request, 'tarefas/editar.html', {'tarefa': tarefa, 'categorias': categorias})

            try:
                categoria = Categoria.objects.get(id=categoria_id)
            except ObjectDoesNotExist:
                messages.error(request, 'Categoria selecionada não existe!')
                return render(request, 'tarefas/editar.html', {'tarefa': tarefa, 'categorias': categorias})

            tarefa.titulo = titulo
            tarefa.descricao = descricao
            tarefa.categoria = categoria
            tarefa.save()
            messages.success(request, 'Tarefa editada com sucesso!')
            return redirect('lista')

        return render(request, 'tarefas/editar.html', {
            'tarefa': tarefa,
            'categorias': categorias
        })
    except ObjectDoesNotExist:
        messages.error(request, 'Tarefa não encontrada!')
        return redirect('lista')
    except Exception as e:
        messages.error(request, f'Erro ao editar tarefa: {str(e)}')
        return redirect('lista')


def deletar_tarefa(request, id):
    try:
        tarefa = Tarefa.objects.get(id=id)
        tarefa_titulo = tarefa.titulo
        tarefa.delete()
        messages.success(request, f'Tarefa "{tarefa_titulo}" deletada com sucesso!')
        return redirect('lista')
    except ObjectDoesNotExist:
        messages.error(request, 'Tarefa não encontrada!')
        return redirect('lista')
    except Exception as e:
        messages.error(request, f'Erro ao deletar tarefa: {str(e)}')
        return redirect('lista')