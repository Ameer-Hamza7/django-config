def write_views_file(MODEL, STRUCTURED_STR):
    with open(f'{MODEL}_view.html', 'a') as f:
        f.write(STRUCTURED_STR)

def ConstructViewHtml(MODEL, *args):
    records = '''
'''
    for x in args:
        records += f'''
            <td>
                [[dataset.{x}]]
            </td>
        '''

    STRING =  f'''
[% load widget_tweaks %]
[% load static %] [% include 'base/head.html' %] [% include 'base/sidebar.html' %] [% include 'base/sidebar.html' %]

<style>

    #example_filter label [
        float: right;
    ]

    #example_paginate ul [
        float: right;
    ]

    .btn [
        font-size: 12px!important;
        padding: 5px 30px!important;
        border-radius: 15px!important;

    ]
    table th [
        text-transform: uppercase;
        font-weight: 600;
        text-align: left!important;
        color: white!important;
    ]
    table.dataTable tr td [
        color: white;
        background-color: transparent!important;
        border-color: #5c5f67!important;
        font-size: 12px;
        padding: 11px 0px 4px 10px!important;
    ]

</style>

<!-- START CONTENT -->
<section id="main-content" class=" ">
    <div class="wrapper main-wrapper row" style=''>

        <div class="clearfix"></div>
        <!-- MAIN CONTENT AREA STARTS -->

        <div class="col-xs-12">
            <section class="box ">
                <header class="panel_header">
                    <h2 class="title pull-left">{MODEL.replace('_', ' ').upper()}</h2>
                    <div class="actions panel_actions pull-right">
                        <a class="box_toggle fa fa-chevron-down"></a>
                        <a class="box_setting fa fa-cog" data-toggle="modal" href="#section-settings"></a>
                        <a class="box_close fa fa-times"></a>
                    </div>
                </header>
                <div class="content-body">
                    <table id="example" class="table table-striped table-bordered" style="width:100%">
                        <thead>
                            <tr>
                               [% for head in header %]
                                <th>[[head]]</th>
                                [% endfor %]
                                <th>Action</th>
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
                                    <a href="[% url 'update_{MODEL.lower()}' dataset.id %]">
                                        <button class="btn btn-secondary" style="margin-right: 5px;">Edit</button>
                                    </a>
                                    <a href="[% url 'delete_{MODEL.lower()}' dataset.id %]">
                                        <button class="btn btn-danger" style="margin-right: 5px;">Delete</button>
                                    </a>

                                </td>
                            </tr>
                            [% endfor %]
                        </tbody>
                    </table>
                </div>
            </section>
        </div>

        <!-- MAIN CONTENT AREA ENDS -->
    </div>
</section>
<!-- END CONTENT -->

[% include 'base/foot.html' %]

<script src="[% static 'assets/plugins/datatables/script1.js' %]"></script>
<script src="[% static 'assets/plugins/datatables/script2.js' %]"></script>

<script>
    $(document).ready(function () [
        $('#example').DataTable();
    ]);
</script>
            '''
    write_views_file(MODEL, STRING)



ConstructViewHtml(
    'Product',
    'product_name',
    'cost_price',
    'sell_price'
)

ConstructViewHtml(
    'Transaction',
    'member',
    'product'
)
