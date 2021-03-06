# Copyright (c) 2016, DjaoDjin inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
# TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
# OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
# OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
# ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from distutils.core import setup

import saas

requirements = []
with open('./requirements.txt') as requirements_txt:
    for line in requirements_txt:
        prerequisite = line.split('#')[0].strip()
        if prerequisite:
            requirements += [prerequisite]

setup(
    name='djaodjin-chat',
    version=chat.__version__,
    author='The DjaoDjin Team',
    author_email='support@djaodjin.com',
    install_requires=requirements,
    packages=['chat',
              'chat.urls',
              'chat.urls.api',
              'chat.managers',
              'chat.views',
              'chat.api',
              ],
    # package_data={'saas': ['fixtures/*',
    #                        'static/js/*.js',
    #                        'templates/saas/*.html',
    #                        'templates/saas/agreements/*.md',
    #                        'templates/saas/app/*.html',
    #                        'templates/saas/billing/*.html',
    #                        'templates/saas/legal/*.html',
    #                        'templates/saas/metrics/*.html',
    #                        'templates/saas/profile/*.html']},
    url='https://github.com/djaodjin/djaodjin-chat/',
    download_url='https://github.com/djaodjin/djaodjin-chat/tarball/%s' \
        % chat.__version__,
    license='BSD',
    description='DjaoDjin Web Chat applicatoin implementation',
    long_description=open('README.md').read(),
)
