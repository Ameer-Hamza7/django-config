# ConstructFormHtml(
#     'Citie',
#     'city'
# )

def write_forms_file(MODEL, STRUCTURED_STR):
    with open(f'{MODEL}_form.html', 'a') as f:
        f.write(STRUCTURED_STR)

def ConstructFormHtml(MODEL, *args):
    fields = ''''''
    for x in args:
        fields += f'''
        
            <div class="col-xs-6" style="margin-bottom : 20px;">
                [% render_field form.{x} class="form-control mb-2" placeholder="{x.replace('_', ' ').upper()}" %]
            </div>
        '''

    STRING =  f'''
[% load widget_tweaks %] [% load static %] [% include 'base/head.html' %] [% include 'base/sidebar.html' %] [% include 'base/sidebar.html' %]

	    <div class="content-wrapper">
			<div class="content-inner">
   				<div class="content">
					<div class="card">
						<div class="card-body">
							<form action="#" method='POST' id="indexForm" enctype="multipart/form-data">
        					 [% csrf_token %]
								<fieldset class="mb-3">
                                    {fields}
								</fieldset>
                                [% if status == 'edit' %]
                                <button class="btn btn-success">UPDATE {MODEL.replace('_', ' ').upper()}</button> [% else %]
                                <button class="btn btn-success">ADD {MODEL.replace('_', ' ').upper()}</button> [% endif %]
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>

[% include 'base/foot.html' %]
            '''
    write_forms_file(MODEL, STRING)


ConstructFormHtml(
    'biometric_machine',
    'serial_no',
    'brand',
    'location',
    'branch'
)
