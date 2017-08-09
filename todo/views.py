from django.shortcuts import render, redirect


from .models import Todo

def index(request):
    todos = Todo.objects.all()

    todos = todos.order_by('prioridad')
    context ={
        'todos': todos
    }
    return render(request, 'index.html', context)

def details(request, id):
    todo = Todo.objects.get(prioridad=id)
    context = {
        'todo': todo
    }
    return render(request, 'details.html', context)

def add(request):
    if(request.method == 'POST'):
        #Aumentamos la prioridad de todos en 1
        todos = Todo.objects.all()
        for todo in todos:
            todo.prioridad = todo.prioridad + 1
            todo.save()

        #creamos el nuevo todo object
        title = request.POST['new_todo']
        todo = Todo(title=title, prioridad=0)
        todo.save()

        return redirect('/todo')
    else:
        return render(request, 'index.html')


def delete(request, id):
    delete_todo = Todo.objects.get(prioridad=id)
    delete_todo.delete()

    int_id = int(id)

    todos = Todo.objects.all()

    for todo in todos:
        id_todo = int(todo.prioridad)
        if(id_todo > int_id):
            id_todo = id_todo - 1
            todo.prioridad = str(id_todo)
            todo.save()



    return redirect('/todo')


def subir(request, id):
    todo_desplazar = Todo.objects.get(prioridad=id)
    if (int(todo_desplazar.prioridad) > 0):
        todo_antes = Todo.objects.get(prioridad= str(int(id)-1))

        prioridad_antes = todo_antes.prioridad
        todo_antes.prioridad = todo_desplazar.prioridad
        todo_antes.save()

        todo_desplazar.prioridad = prioridad_antes
        todo_desplazar.save()

    return redirect('/todo')


def bajar(request, id):
    todos = Todo.objects.all()
    count_elements = todos.count()

    todo_desplazar = Todo.objects.get(prioridad=id)

    if (int(todo_desplazar.prioridad) < count_elements - 1):
        todo_despues = Todo.objects.get(prioridad=str(int(id)+1))

        prioridad_despues = todo_despues.prioridad
        todo_despues.prioridad = todo_desplazar.prioridad
        todo_despues.save()

        todo_desplazar.prioridad = prioridad_despues
        todo_desplazar.save()

    return redirect('/todo')