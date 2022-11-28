# -*- coding: utf-8 -*-
{
    'name': "course_reg",

    'description': """
        Course Registration
    """,

    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale'],

    'data': [
        "views/course.xml",
        "security/ir.model.access.csv",
        "views/res_partner.xml",
    ],
}
