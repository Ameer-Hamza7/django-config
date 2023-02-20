def write_views_file(MODEL, STRUCTURED_STR):
    with open(f'app_forms/{MODEL}_form.html', 'a') as f:
        f.write(STRUCTURED_STR)


def write_individual_view_file(MODEL, STRUCTURED_STR):
    with open(f'app_views/{MODEL}_view.html', 'a') as f:
        f.write(STRUCTURED_STR)


app_name = 'employee_app'


def ConstructViewHtml(MODEL, views, fields, models):
    forms = '''
    '''

    for y in fields:
        print('f', y)
        forms += f'''
            <div class="col-lg-6" style="margin-bottom : 20px;">
                <fieldset>

                    <div class="form-group">
                        <label>[[form.{y}.label]]</label>
                        [% render_field form.{y} class="form-control mb-2" placeholder="{y.replace('_', ' ').upper()}" %]
                    </div>

                </fieldset>
            </div>
        '''

        tags = '''
'''
    for x in views:
        tags += f'''
            <td>
                [[dataset.{x}]]
            </td>
        '''

    records = '''
'''
    for x in views:
        print(x)
        records += f'''
            <td>
                [[dataset.{x}]]
            </td>
        '''

    navs = '''
    '''
    for x in models:
        navs += f'''
            [% if perms.{app_name}.view_{x} %]
            <li class="nav-item">
                <a href="[% url 'create_{x}' %]" class="nav-link {'active' if x == MODEL else ''}">
                    {x.replace('_', ' ').upper()}S
                </a>
            </li>
            [% endif %]
        '''

    STRING = f'''
[% load widget_tweaks %]
[% load static %] [% include 'base/head.html' %] [% include 'base/sidebar-left.html' %]
<div class="content-wrapper">
  <!-- Page header -->
  <div class="page-header page-header-light">
    <ul class="nav nav-tabs nav-tabs-bottom" style="margin-bottom: 0px">
      {navs}
    </ul>
  </div>
  <!-- /page header -->

  <!-- Inner content -->
  <div class="content-inner">
    <!-- Content area -->
    <div class="content">
      [% if status == 'edit' %]
      <div class="card">
        <div class="card-body">
            <form method='POST' enctype="multipart/form-data">
                [% csrf_token %]
                <div class="row">
                    {forms}
                </div>
                <div class="text-right">
                    [% if status == 'edit' %]
                    <button class="btn btn-success">UPDATE {MODEL.replace('_', ' ').upper()}</button> [% else %]
                    <button class="btn btn-success">ADD {MODEL.replace('_', ' ').upper()}</button> [% endif %]
                </div>
            </form>
        </div>
      </div>
      [% endif %]
      [% if status == 'add' %]
      <div class="card">
        <div class="card-header">
          <h5 class="card-title">{MODEL.replace('_', ' ').upper()}</h5>
        </div>

        <table class="table datatable-column-search-selects">
          <thead>
            <tr>
              [% for head in header %]
              <th>[[head]]</th>
              [% endfor %]
              <th>ACTIONS</th>
            </tr>
          </thead>
          <tbody>
            [% for dataset in data %]
            <tr>
                <td>
                    [[dataset.id]]
                </td>
                {records}
                <td style="padding: 5px 10px!important">
                    [% if perms.{app_name}.view_{MODEL} %]
                    <a href="[% url 'view_{MODEL.lower()}' dataset.id %]">
                        <button class="btn btn-success" style="margin-right: 5px;"><i class="fas fa-eye fa-xl"></i></button>
                    </a>
                    [% endif %]
                    [% if perms.{app_name}.change_{MODEL} %]
                    <a href="[% url 'update_{MODEL.lower()}' dataset.id %]">
                        <button class="btn btn-secondary" style="margin-right: 5px;"><i class="fas fa-edit fa-xl"></i></button>
                    </a>
                    [% endif %]
                    [% if perms.{app_name}.delete_{MODEL} %]
                    <a href="[% url 'delete_{MODEL.lower()}' dataset.id %]">
                        <button class="btn btn-danger" style="margin-right: 5px;"><i class="fas fa-trash fa-xl"></i></button>
                    </a>
                    [% endif %]
                </td>
            </tr>
            [% endfor %]
          </tbody>
        </table>
      </div>
      [% endif %]
    </div>
    <!-- /content area -->
  </div>
  <!-- /inner content -->
</div>
<div
  class="sidebar sidebar-light sidebar-right sidebar-expand-xl sidebar-collapsed"
>
  <!-- Expand button -->
  <button
    type="button"
    class="btn btn-sidebar-expand sidebar-control sidebar-right-toggle"
  >
    <i class="icon-arrow-left12"></i>
  </button>
  <!-- /expand button -->

  <!-- Sidebar content -->
  [% if status == 'add' %]
  <div class="sidebar-content">
    <!-- Header -->
    <div class="sidebar-section sidebar-section-body d-flex align-items-center">
      [% if status == 'edit' %]
      <h5 class="mb-0">UPDATE {MODEL.replace('_', ' ').upper()}</h5>
      [% else %]
      <h5 class="mb-0">ADD {MODEL.replace('_', ' ').upper()}</h5>
      [% endif %]

      <div class="ml-auto">
        <button
          type="button"
          class="btn btn-outline-light text-body border-transparent btn-icon rounded-pill btn-sm sidebar-control sidebar-right-toggle d-none d-xl-inline-block"
        >
          <i class="icon-transmission"></i>
        </button>

        <button
          type="button"
          class="btn btn-outline-light text-body border-transparent btn-icon rounded-pill btn-sm sidebar-mobile-right-toggle d-xl-none"
        >
          <i class="icon-cross2"></i>
        </button>
      </div>
    </div>
    <!-- /header -->
    <!-- Actions -->
    [% if perms.{app_name}.add_{MODEL} %]
    <div class="sidebar-section">
      <div id="sidebar-actions">
        <div class="sidebar-section-body">
            <div class="card">
                <div class="card-body">
                    <form method='POST' enctype="multipart/form-data">
                        [% csrf_token %]
                        <div class="row">
                            {forms}
                        </div>
                        <div class="text-right">
                            [% if status == 'edit' %]
                            <button class="btn btn-success">UPDATE {MODEL.replace('_', ' ').upper()}</button> [% else %]
                            <button class="btn btn-success">ADD {MODEL.replace('_', ' ').upper()}</button> [% endif %]
                        </div>
                    </form>
                </div>
            </div>
        </div>
      </div>
    </div>
    [% endif %]
  </div>
  [% endif %]
  <!-- /sidebar content -->
</div>

[% include 'base/foot.html' %]
            '''
    write_views_file(MODEL, STRING)


def ConstructIndividualView(MODEL, details, models):

    navs = '''
  '''
    for x in models:
        navs += f'''
          <li class="nav-item">
              <a href="[% url 'create_{x}' %]" class="nav-link {'active' if x == MODEL else ''}">
                  {x.replace('_', ' ').upper()}S
              </a>
          </li>
      '''

    fields = '''
  '''

    for x in details:
        fields += f'''
          <div class="col-sm-6">
            <div class="mb-4">
              <dl>
                <dt
                  class="font-size-sm font-weight-bold text-uppercase"
                >
                  {x.replace('_', ' ').upper()}
                </dt>
                <dd>
                  [[data.{x}]]
                </dd>
              </dl>
            </div>
          </div>
    '''

    STRING = f'''
  [% load widget_tweaks %]
[% load static %] [% include 'base/head.html' %] [% include 'base/sidebar-left.html' %]
    <!-- Main content -->
    <div class="content-wrapper">
      <div class="page-header page-header-light">
        <ul class="nav nav-tabs nav-tabs-bottom" style="margin-bottom: 0px">
          {navs}
        </ul>
      </div>

      <!-- Inner content -->
      <div class="content-inner">
        <!-- Content area -->
        <div class="content">
          <!-- Course overview -->
          <div class="card">
            <div class="card-header header-elements-lg-inline">
              <h5 class="card-title">{MODEL.replace('_', ' ').upper()}</h5>

              <div class="header-elements">
                <button
                  class="btn btn-success"
                  style="margin-right: 5px"
                  onclick="printPage()"
                >
                  <i class="fas fa-eye fa-xl"></i>
                </button>
                <a href="[% url 'update_{MODEL}' data.id %]">
                  <button class="btn btn-secondary" style="margin-right: 5px">
                    <i class="fas fa-edit fa-xl"></i>
                  </button>
                </a>
                <a href="[% url 'delete_{MODEL}' data.id %]">
                  <button class="btn btn-danger" style="margin-right: 5px">
                    <i class="fas fa-trash fa-xl"></i>
                  </button>
                </a>
              </div>
            </div>

            <div class="nav-tabs-responsive bg-light border-top"></div>

            <div class="tab-content">
              <div class="tab-pane fade show active" id="course-overview">
                <div class="card-body">
                  <div class="row">
                    {fields}
                  </div>
                </div>
              </div>
            </div>
          </div>
          <!-- /course overview -->
        </div>
        <!-- /content area -->
      </div>
      <!-- /inner content -->
    </div>
    <!-- /main content -->
  <script>
    function printPage() [
      print();
    ]
  </script>
  <!-- /page content -->
'''

    write_individual_view_file(MODEL, STRING)

# ========================= Depends Upon every Django App


# {% if perms.accounts.view_expense_ledger %}
models = [
    'disciplinary_action'
]

# ========================= Depends Upon every Django App


# ========================= Depends Upon every Django Model

# Tables Headers and Grid ( admin.py ===> list_display ===> remove id )
views = ['employee', 'serial_no', 'manager',
         'infraction_date', 'infraction_time']

fields = [
    'employee',
    'emp_cl_id',
    'emp_pos',
    'manager',
    'manager_cl_id',
    'emp_pos',
    'infraction_date',
    'infraction_time',
    'infraction_place',
    'infraction_desc',
    'emp_stat',
    'proposed_corrective_action',
    'employee_print_name',
    'employee_sig',
    'emp_sig_date',
    'manager_print_name',
    'manager_sig',
    'manager_sig_date',
    'hr_print_name',
    'hr_sig',
    'hr_sig_date'
]

ConstructViewHtml(
    'disciplinary_action',
    views=views,
    fields=fields,
    models=models
)

ConstructIndividualView(
    'disciplinary_action',
    fields,
    models
)

# ========================= Depends Upon every Django Model

# # Tables Headers and Grid ( admin.py ===> list_display ===> remove id )
# views = ['employee','asset', 'in_emp_use', 'allowed_for']

# fields = [
#     'employee',
#     'asset',
#     'in_emp_use',
#     'allowed_for',
# ]

# ConstructViewHtml(
#     'employee_asset',
#     views=views,
#     fields=fields,
#     models=models
# )

# ConstructIndividualView(
#     'employee_asset',
#     fields,
#     models
# )

# # ========================= Depends Upon every Django Model

# # Tables Headers and Grid ( admin.py ===> list_display ===> remove id )
# views = ['machine_gen_user_id','user_name', 'tag_id']

# fields = [
#       'machine_gen_user_id',
#       'user_name',
#       'tag_id',
# ]

# ConstructViewHtml(
#     'employee_biometric_record',
#     views=views,
#     fields=fields,
#     models=models
# )

# ConstructIndividualView(
#     'employee_biometric_record',
#     fields,
#     models
# )

# # ========================= Depends Upon every Django Model
# # ========================= Depends Upon every Django Model

# # Tables Headers and Grid ( admin.py ===> list_display ===> remove id )
# views = ['employee',
#                     'termination_date', 'amount_payable', 'amount_recieveable']

# fields = [
#       'employee',
#       'termination_date',
#       'component_payable',
#       'ref_doc_type_payable',
#       'amount_payable',
#       'status_payable',
#       'ref_doc_type_recieveable',
#       'component_recieveable',
#       'amount_recieveable',
#       'status_recieveable',
#       'reference',
#       'assets',
#       'asset_returns',
# ]

# ConstructViewHtml(
#     'company_employe_termination',
#     views=views,
#     fields=fields,
#     models=models
# )

# ConstructIndividualView(
#     'company_employe_termination',
#     fields,
#     models
# )

# # ========================= Depends Upon every Django Model
# # Tables Headers and Grid ( admin.py ===> list_display ===> remove id )
# views = ['employee',
#                     'prev_designation', 'new_designation', 'prev_dept', 'new_dept', 'promotion_date']

# fields = [
#       'employee',
#       'previous_branch',
#       'promoted_branch',
#       'prev_designation',
#       'new_designation',
#       'prev_dept',
#       'new_dept',
#       'promotion_date',
# ]

# ConstructViewHtml(
#     'employee_promotion',
#     views=views,
#     fields=fields,
#     models=models
# )

# ConstructIndividualView(
#     'employee_promotion',
#     fields,
#     models
# )

# # ========================= Depends Upon every Django Model
# # Tables Headers and Grid ( admin.py ===> list_display ===> remove id )
# views = ['employee','appraisal_title', 'status', 'appraisal_goal', 'start_date', 'end_date']

# fields = [
#     'employee',
#     'appraisal_title',
#     'status',
#     'start_date',
#     'end_date',
#     'appraisal_goal',
# ]

# ConstructViewHtml(
#     'employee_appraisal',
#     views=views,
#     fields=fields,
#     models=models
# )

# ConstructIndividualView(
#     'employee_appraisal',
#     fields,
#     models
# )


# app_name = 'root_app'


# models = [
#       'company_setup',
#       'company_branche',
#       'company_skill',
#       'company_dept',
#       'company_designation',
#       'branch_image',
#       'company_asset',
#       'asset_shifting',
#       'language_setting',
#       'notification',

# ]

# # ========================= Depends Upon every Django App


# # ========================= Depends Upon every Django Model

# # Tables Headers and Grid ( admin.py ===> list_display ===> remove id )
# views = [ 'company_name',
#                     'comapny_name_ar', 'company_coc_id', 'country', 'domain']

# fields = [
#     'company_name',
#     'comapny_name_ar',
#     'tax_id',
#     'domain',
#     'company_coc_id',
#     'company_web_ur',
#     'default_currency',
#     'establishment_data',
#     'country',
#     'parent_comapny',
#     'company_logo',
# ]

# ConstructViewHtml(
#     'company_setup',
#     views=views,
#     fields=fields,
#     models=models
# )

# ConstructIndividualView(
#     'company_setup',
#     fields,
#     models
# )

# # ========================= Depends Upon every Django Model

# # Tables Headers and Grid ( admin.py ===> list_display ===> remove id )
# views = ['company',
#                     'branch_name', 'branch_name_ar', 'head_office', 'branch_incharge_name']

# fields = [
#     'company',
#     'branch_name',
#     'branch_name_ar',
#     'branch_code',
#     'branch_incharge_name',
#     'address',
#     'branch_type',
#     'head_office',
#     'latitude',
#     'longitude',
#     'branch_logo',
#     'description',
# ]

# ConstructViewHtml(
#     'company_branche',
#     views=views,
#     fields=fields,
#     models=models
# )

# ConstructIndividualView(
#     'company_branche',
#     fields,
#     models
# )

# # ========================= Depends Upon every Django Model

# # Tables Headers and Grid ( admin.py ===> list_display ===> remove id )
# views = [ 'skill_title','skill_title_ar', 'creted', 'modified']


# fields = [
#     'skill_title',
#     'skill_title_ar',
#     'parent_skill',
# ]

# ConstructViewHtml(
#     'company_skill',
#     views=views,
#     fields=fields,
#     models=models
# )

# ConstructIndividualView(
#     'company_skill',
#     fields,
#     models
# )

# # ========================= Depends Upon every Django Model

# # Tables Headers and Grid ( admin.py ===> list_display ===> remove id )
# views = [ 'company','dept_title', 'dept_title_ar', 'creted']

# fields = [
#     'company',
#     'dept_title',
#     'dept_title_ar',
#     'parent_dept',
#     'dept_objective',
#     'dept_success',
#     'dept_minimum_performance_level',
# ]

# ConstructViewHtml(
#     'company_dept',
#     views=views,
#     fields=fields,
#     models=models
# )

# ConstructIndividualView(
#     'company_dept',
#     fields,
#     models
# )

# # ========================= Depends Upon every Django Model

# # Tables Headers and Grid ( admin.py ===> list_display ===> remove id )
# views = [
#     'company',
#     'department',
#     'designation_title',
#     'report_to_designation',]

# fields = [
#     'company',
#     'department',
#     'designation_title',
#     'designation_title_ar',
#     'report_to_designation',
#     'job_desc',
# ]

# ConstructViewHtml(
#     'company_designation',
#     views=views,
#     fields=fields,
#     models=models
# )

# ConstructIndividualView(
#     'company_designation',
#     fields,
#     models
# )

# # ========================= Depends Upon every Django Model

# # Tables Headers and Grid ( admin.py ===> list_display ===> remove id )
# views = [ 'branch',
#     'image',]

# fields = [
#     'branch',
#     'image',
# ]

# ConstructViewHtml(
#     'branch_image',
#     views=views,
#     fields=fields,
#     models=models
# )

# ConstructIndividualView(
#     'branch_image',
#     fields,
#     models
# )

# # ========================= Depends Upon every Django Model

# # Tables Headers and Grid ( admin.py ===> list_display ===> remove id )
# views = ['company',
#       'branch',
#       'asset_owner',
#       'item_code',]

# fields = [
#       'company',
#       'branch',
#       'asset_owner',
#       'item_code',
#       'asset_title',
#       'asset_desc',
#       'location',
#       'asset_status',
#       'custodian',
#       'asset_image',
#       'dept',
#       'asset_desc',
#       'warehouse',
#       'asset_type',
#       'purchase_date',
#       'purchase_invoice',
#       'purchase_receipt',
#       'vendor_name',
#       'vendor_details',
# ]

# ConstructViewHtml(
#     'company_asset',
#     views=views,
#     fields=fields,
#     models=models
# )

# ConstructIndividualView(
#     'company_asset',
#     fields,
#     models
# )

# # ========================= Depends Upon every Django Model

# # Tables Headers and Grid ( admin.py ===> list_display ===> remove id )
# views = [ 'asset',
#     'from_branch',
#     'from_location',
#     'to_branch']

# fields = [
#     'asset',
#     'from_branch',
#     'from_location',
#     'to_branch',
#     'to_location',
#     'reason',
# ]

# ConstructViewHtml(
#     'asset_shifting',
#     views=views,
#     fields=fields,
#     models=models
# )

# ConstructIndividualView(
#     'asset_shifting',
#     fields,
#     models
# )

# # ========================= Depends Upon every Django Model

# # Tables Headers and Grid ( admin.py ===> list_display ===> remove id )
# views = ['in_eng',
#     'in_arabic',
#     'tag_code',]

# fields = [
#     'in_eng',
#     'in_arabic',
#     'tag_code',
# ]

# ConstructViewHtml(
#     'language_setting',
#     views=views,
#     fields=fields,
#     models=models
# )

# ConstructIndividualView(
#     'language_setting',
#     fields,
#     models
# )

# # ========================= Depends Upon every Django Model

# # Tables Headers and Grid ( admin.py ===> list_display ===> remove id )
# views = ['send_by',
#     'audience',
#     'message_title',
#     'message',]

# fields = [
#     'send_by',
#     'audience',
#     'message_title',
#     'message',
# ]

# ConstructViewHtml(
#     'notification',
#     views=views,
#     fields=fields,
#     models=models
# )

# ConstructIndividualView(
#     'notification',
#     fields,
#     models
# )

# # ========================= Depends Upon every Django Model


# app_name = 'attendance_app'

# models = [
#     'shift',
#     'overtime',
#     'employee_punch',
#     'shift_assignment',
#     'attendance_status_code',
#     'attendance_log',
#     'biometric_attendance_record',

# ]

# # ========================= Depends Upon every Django App


# # ========================= Depends Upon every Django Model

# # Tables Headers and Grid ( admin.py ===> list_display ===> remove id )
# views = ['shift_title', 'shift_type',
#          'start_time', 'end_time', 'total_hours']

# fields = [
#     'shift_title',
#     'shift_type',
#     'start_time',
#     'end_time',
#     'max_overtime',
#     'overtime_duration',
#     'allow_late_arrival',
#     'allow_early_departure',
#     'total_hours',
# ]

# ConstructViewHtml(
#     'shift',
#     views=views,
#     fields=fields,
#     models=models
# )

# ConstructIndividualView(
#     'shift',
#     fields,
#     models
# )

# # ========================= Depends Upon every Django Model

# # Tables Headers and Grid ( admin.py ===> list_display ===> remove id )
# views = ['employee', 'shift_type',
#          'status']

# fields = [
#     'employee',
#     'shift_type',
#     'status',

# ]

# ConstructViewHtml(
#     'shift_assignment',
#     views=views,
#     fields=fields,
#     models=models
# )

# ConstructIndividualView(
#     'shift_assignment',
#     fields,
#     models
# )

# # ========================= Depends Upon every Django Model

# # Tables Headers and Grid ( admin.py ===> list_display ===> remove id )
# views = ['attendancec_code', 'code_desc',
#          'created']

# fields = [
# 'attendancec_code',
# 'code_desc',
# 'created',
# 'modified',
# ]

# ConstructViewHtml(
#     'attendance_status_code',
#     views=views,
#     fields=fields,
#     models=models
# )

# ConstructIndividualView(
#     'attendance_status_code',
#     fields,
#     models
# )

# # ========================= Depends Upon every Django Model

# # Tables Headers and Grid ( admin.py ===> list_display ===> remove id )
# views = ['employee', 'attendance_date',
#          'check_in_time', 'check_out_time', 'attendance_code']

# fields = [
#       'employee',
#       'attendance_date',
#       'check_in_time',
#       'check_out_time',
#       'overtime_start',
#       'overtime_end',
#       'attendance_code',
#       'late',
# ]

# ConstructViewHtml(
#     'attendance_log',
#     views=views,
#     fields=fields,
#     models=models
# )

# ConstructIndividualView(
#     'attendance_log',
#     fields,
#     models
# )

# # ========================= Depends Upon every Django Model

# # ========================= Depends Upon every Django Model

# # Tables Headers and Grid ( admin.py ===> list_display ===> remove id )
# views = ['employee', 'machine_based_user_id',
#          'timestamp', 'flag', 'flag_attendance_type']

# fields = [
#     'employee',
#     'machine_based_user_id',
#     'timestamp',
#     'flag',
#     'flag_attendance_type',
# ]

# ConstructViewHtml(
#     'biometric_attendance_record',
#     views=views,
#     fields=fields,
#     models=models
# )

# ConstructIndividualView(
#     'biometric_attendance_record',
#     fields,
#     models
# )

# # ========================= Depends Upon every Django Model


# app_name = 'payroll_app'

# models = [
#     'employee_basic_salarie',
#     'salary_log',
# ]

# # ========================= Depends Upon every Django App


# # ========================= Depends Upon every Django Model

# # Tables Headers and Grid ( admin.py ===> list_display ===> remove id )
# views = ['employee', 'basic_salary',
#          'currency', 'active']

# fields = [
#     'employee',
#     'basic_salary',
#     'currency',
#     'housing_allowance_per',
#     'transport_allowance_per',
#     'mobile_allowance_per',
#     'gosi_per',
#     'gosi_constant',
#     'per_hour_rate',
#     'overtime_constant',
#     'active',
# ]

# ConstructViewHtml(
#     'employee_basic_salarie',
#     views=views,
#     fields=fields,
#     models=models
# )

# ConstructIndividualView(
#     'employee_basic_salarie',
#     fields,
#     models
# )

# # ========================= Depends Upon every Django Model
# # Tables Headers and Grid ( admin.py ===> list_display ===> remove id )
# views = ['month', 'year',
#          'basic_salary', 'net_salary']

# fields = [
#       'month',
#       'year',
#       'basic_salary',
#       'days_criteria',
#       'net_basic_salary',
#       'transport_allw',
#       'housing_allw',
#       'mobile_allw',
#       'other_earnings',
#       'gross_salary',
#       'annual_leaves',
#       'gross_earnings',
#       'gosi',
#       'other_deductions',
#       'gross_deduction',
#       'net_salary',
# ]

# ConstructViewHtml(
#     'salary_log',
#     views=views,
#     fields=fields,
#     models=models
# )

# ConstructIndividualView(
#     'salary_log',
#     fields,
#     models
# )

# # ========================= Depends Upon every Django Model
