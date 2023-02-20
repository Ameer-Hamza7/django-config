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

    STRING = f'''
[% load widget_tweaks %] [% load static %] [% include 'base/head.html' %] [% include 'base/sidebar.html' %] [% include 'base/sidebar.html' %]

<!-- START CONTENT -->
<section id="main-content" class=" ">
    <div class="wrapper main-wrapper row" style=''>

        <div class="clearfix"></div>
        <!-- MAIN CONTENT AREA STARTS -->

        <div class="col-xs-12">
            <section class="box ">
                <header class="panel_header">
                    [% if status == 'edit' %]
                    <h2 class="title pull-left">UPDATE {MODEL.replace('_', ' ').upper()}</h2>
                    [% else %]
                    <h2 class="title pull-left">ADD {MODEL.replace('_', ' ').upper()}</h2>
                    [% endif %]
                    <div class="actions panel_actions pull-right">
                        <a class="box_toggle fa fa-chevron-down"></a>
                        <a class="box_setting fa fa-cog" data-toggle="modal" href="#section-settings"></a>
                        <a class="box_close fa fa-times"></a>
                    </div>
                </header>
                <div class="content-body">
                    <form method="POST" enctype="multipart/form-data">
                        [% csrf_token %]
                        <!-- START -->
                        <div class='row'>
                            {fields}
                        </div>
                        <br>
                        <!-- END -->
                        [% if status == 'edit' %]
                        <button class="btn btn-success">UPDATE {MODEL.replace('_', ' ').upper()}</button> [% else %]
                        <button class="btn btn-success">ADD {MODEL.replace('_', ' ').upper()}</button> [% endif %]
                    </form>
                </div>
            </section>
        </div>

        <!-- MAIN CONTENT AREA ENDS -->
    </div>
</section>
<!-- END CONTENT -->

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
