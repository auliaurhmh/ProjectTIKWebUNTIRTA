from django.shortcuts import render, redirect
from faperta.models import Dosen, Staf, Mahasiswa
from faperta.form import FormDosen, FormStaf, FormMahasiswa
from django.contrib import messages


# Create your views here.
def hapus_dosen(request, id_dosen):
    dosen = Dosen.objects.filter(id=id_dosen)
    dosen.delete()

    messages.success(request, "Data Berhasil Dihapus!")
    return redirect('dosen')

def ubah_dosen(request, id_dosen):
    dosen = Dosen.objects.get(id=id_dosen)
    template = 'ubah-dosen.html'
    if request.POST:
        form = FormDosen(request.POST, instance=dosen)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil Diperbaharui!")
            return redirect('ubah-dosen', id_dosen=id_dosen)
    else:
        form = FormDosen(instance=dosen)
        konteks = {
            'form':form,
            'dosen':dosen,
        }    

    return render(request, template, konteks)    

def indexfaperta(request):
    return render(request, 'fapertamuka.html')


def tambah_dosen(request):
    if request.POST:
        form = FormDosen(request.POST)
        if form.is_valid():
            form.save()
            form =FormDosen()
            pesan = "Data Berhasil Disimpan"

            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'tambah-dosen.html', konteks)

    else:
        form = FormDosen()
   
    konteks = {
        'form': form,
    }

    return render(request, 'tambah-dosen.html', konteks)

def tambah_staf(request):
     if request.POST:
        form = FormStaf(request.POST)
        if form.is_valid():
            form.save()
            form =FormStaf()
            pesan = "Data Berhasil Disimpan"

            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'tambah-staf.html', konteks)

        else:
         form = FormStaf()

        konteks = {
        'form': form,
         }

        return render(request, 'tambah-staf.html', konteks)

def tambah_mahasiswa(request):
    if request.POST:
        form = FormMahasiswa(request.POST)
        if form.is_valid():
            form.save()
            form = FormMahasiswa()
            pesan = "Data Berhasil Disimpan"

            konteks = {
                'form' : form,
                'pesan': pesan,
            }

            return render (request, 'tambah-mahasiswa.html', konteks)
    else: 
        form = FormMahasiswa()

    konteks = {
        'form': form
    }

    return render(request, 'tambah-mahasiswa.html', konteks)