from django.contrib.auth.models import Group

def doctor(id,uid):
    x = uid
    id['Appointments'] = '/schedule'
    id['Cases'] = '/case'
    return id

def in_reception(id,uid):
    x = uid
    id['New Patient'] = '/profile/register'
    id['Manage Appointments'] = '/appointments'
    id['New Appointment'] = '/appointments/book'
    id['Bills'] = '/bill'
    id['Cases'] = '/case'
    id['Generate Case'] = '/case/generate'
    return id

def patient(id,uid):
    x = uid
    id['Reports'] = '/reports'
    id['Appointments'] = '/appointments'
    id['Medication'] = '/bill/medicines'
    id['Bills'] = '/bill'
    id['Cases'] = '/case'
    return id

def nurse(id,uid):
    x = uid
    id['Reports'] = '/reports'
    id['Generate Report'] = '/reports/generate'
    return id

def medicos_manager(id,uid):
    x = uid
    menu['All Stock'] = ''
    menu['Stock Details'] = ''
    return id

def Url_found(ufo, url):
    group = Group.objects.get(name=url)
    return True if group in ufo.groups.all() else False

def menu_processor(request):
    menu = {}
    user = request.user
    modules_hms = ['patient','doctor','inventory_manager','lab_attendant','receptionist']
    if Url_found(user,modules_hms[0] ):
        menu = patient(menu,user)
    elif Url_found(user,modules_hms[1] ):
        menu = doctor(menu,user)    
    elif Url_found(user,modules_hms[2] ):
        menu = medicos_manager(menu,user)  
    elif Url_found(user,modules_hms[3] ):
        menu = nurse(menu,user)            
    elif Url_found(user,modules_hms[4] ):
        menu = in_reception(menu,user)
    return {'menu': menu}
