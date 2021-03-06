from django.http import HttpResponse
from django.template import Context, loader
from employees.models import Employee, EmployeeForm
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.forms.models import modelformset_factory
def ip_address_processor(request):
    return {'ip_address': request.META['REMOTE_ADDR']}

def index(request):
    all_employees = Employee.objects.all()
    t = loader.get_template('employees/index.html')
    c = RequestContext(request, {
        'all_employees': all_employees,
	}, [ip_address_processor])
    return HttpResponse(t.render(c))


def addEmployee(request):
	form = EmployeeForm(request.POST or None)
	if form.is_valid():
		emodel = form.save()
		emodel.save()
		return redirect(index)
	return render_to_response('employees/addEmployee.html', {'employee_form': form}, context_instance=RequestContext(request))
