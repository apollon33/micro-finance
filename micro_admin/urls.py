from django.conf.urls import url
from micro_admin.views import *

urlpatterns = [

    url(r'^$', index, name='microadmin_index'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$',
        LogoutView.as_view(),
        name="logout"),
    # ------------------------------------------- #
    # Branch model urls
    url(r'^branch/create/$',
        CreateBranchView.as_view(),
        name='createbranch'),
    url(r'^branch/edit/(?P<pk>\d+)/$',
        UpdateBranchView.as_view(),
        name='editbranch'),
    url(r'^branch/view/$',
        BranchListView.as_view(),
        name='viewbranch'),
    url(r'^branch/delete/(?P<pk>\d+)/$',
        BranchInactiveView.as_view(),
        name='deletebranch'),
    url(r'^branch/profile/(?P<pk>\d+)/$',
        BranchProfileView.as_view(),
        name='branchprofile'),
    # ------------------------------------------- #
    # User model urls
    url(r'^user/edit/(?P<pk>\d+)/$',
        UpdateUserView.as_view(),
        name='edituser'),
    url(r'^user/create/$',
        CreateUserView.as_view(),
        name='createuser'),
    url(r'^user/profile/(?P<pk>\d+)/$',
        UserProfileView.as_view(),
        name='userprofile'),
    url(r'^users/list/$',
        UsersListView.as_view(),
        name='userslist'),
    url(r'^user/delete/(?P<pk>\d+)/$',
        UserInactiveView.as_view(),
        name='deleteuser'),
    # ------------------------------------------- #
    # Client model urls
    url(r'^client/create/$',
        CreateClientView.as_view(),
        name='createclient'),
    url(r'^client/edit/(?P<pk>\d+)/$',
        UpdateClientView.as_view(),
        name='editclient'),
    url(r'^clients/list/$',
        ClientsListView.as_view(),
        name='viewclient'),
    url(r'^client/profile/(?P<pk>\d+)/$',
        ClienProfileView.as_view(),
        name='clientprofile'),
    url(r'^client/delete/(?P<pk>\d+)/$',
        ClientInactiveView.as_view(),
        name='deleteclient'),
    url(r'^client/profile/update/(?P<client_id>\d+)/$',
        update_clientprofile, name='updateclientprofile'),
    # ------------------------------------------- #
    # Group
    url(r'^group/create/$', CreateGroupView.as_view(), name='creategroup'),
    url(r'^group/profile/(?P<group_id>\d+)/$', GroupProfileView.as_view(),
        name='groupprofile'),
    url(r'^groupslist/$', groups_list, name='groupslist'),
    url(r'^deletegroup/(?P<group_id>\d+)/$', delete_group, name='deletegroup'),
    url(r'^group/(?P<group_id>\d+)/assign-staff/$',
        GroupAssignStaffView.as_view(), name='assignstaff'),

    # Group Members (add, remove, view)
    url(r'^group/(?P<group_id>\d+)/members/add/$',
        GroupAddMembersView.as_view(), name='addmember'),
    url(r'^viewmembers/(?P<group_id>\d+)/$',
        viewmembers_under_group, name='viewmembers'),
    url(r'^removemember/(?P<group_id>\d+)/(?P<client_id>\d+)/$',
        removemembers_from_group, name='removemember'),
    url(r'^groupmeetings/(?P<group_id>\d+)/$',
        group_meetings, name='groupmeetings'),
    url(r'^addgroupmeeting/(?P<group_id>\d+)/$',
        add_group_meeting, name='addgroupmeeting'),
    url(r'^clientsavingsapplication/(?P<client_id>\d+)/$',
        client_savings_application, name='clientsavingsapplication'),
    url(r'^clientsavingsaccount/(?P<client_id>\d+)/$',
        client_savings_account, name='clientsavingsaccount'),
    url(r'^groupsavingsapplication/(?P<group_id>\d+)/$',
        group_savings_application, name='groupsavingsapplication'),
    url(r'^groupsavingsaccount/(?P<group_id>\d+)/$',
        group_savings_account, name='groupsavingsaccount'),
    # savings account status
    url(r'^savings-account/status/(?P<savingsaccount_id>\d+)/$',
        change_savings_account_status, name='savings_account_status'),
    url(r'^viewgroupsavingsdeposits/(?P<group_id>\d+)/$',
        ViewGroupSavingsDeposits.as_view(),
        name='viewgroupsavingsdeposits'),
    url(r'^viewgroupsavingswithdrawals/(?P<group_id>\d+)/$',
        ViewGroupSavingsWithdrawals.as_view(),
        name='viewgroupsavingswithdrawals'),
    url(r'^group/loan/application/(?P<group_id>\d+)/$',
        GroupLoanApplicationView.as_view(), name='grouploanapplication'),
    url(r'^grouploanaccount/(?P<pk>\d+)/$',
        GroupLoanAccount.as_view(),
        name='grouploanaccount'),
    url(r'^client/loan/application/(?P<client_id>\d+)/$',
        ClientLoanApplicationView.as_view(),
        name='clientloanapplication'),
    url(r'^clientloanaccount/(?P<pk>\d+)/$',
        ClientLoanAccount.as_view(),
        name='clientloanaccount'),
    url(r'^loan-account/status/(?P<pk>\d+)/$',
        ChangeLoanAccountStatus.as_view(),
        name='change_loan_account_status'),
    url(r'^listofclientloandeposits/(?P<client_id>\d+)/(?P<loanaccount_id>\d+)/$',
        ListOfClientLoanDeposits.as_view(),
        name='listofclientloandeposits'),
    url(r'^listofclientsavingsdeposits/(?P<client_id>\d+)/$',
        ListOfClientSavingsDeposits.as_view(),
        name='listofclientsavingsdeposits'),
    url(r'^listofclientsavingswithdrawals/(?P<client_id>\d+)/$',
        ListOfClientSavingsWithdrawals.as_view(),
        name='listofclientsavingswithdrawals'),
    url(r'^viewgrouploandeposits/(?P<group_id>\d+)/(?P<loanaccount_id>\d+)/$',
        ViewGroupLoanDiposits.as_view(),
        name='viewgrouploandeposits'),
    url(r'^issueloan/(?P<loanaccount_id>\d+)/$',
        IssueLoan.as_view(),
        name='issueloan'),
    url(r'^receiptsdeposit/$', receipts_deposit, name="receiptsdeposit"),
    url(r'^receiptslist/$',
        ReceiptsList.as_view(),
        name="receiptslist"),
    url(r'^ledgeraccount/(?P<client_id>\d+)/(?P<loanaccount_id>\d+)/$',
        LedgerAccount.as_view(),
        name="ledgeraccount"),
    url(r'^generalledger/$',
        GeneralLedger.as_view(),
        name="generalledger"),
    url(r'^fixeddeposits/$', fixed_deposits, name="fixeddeposits"),
    url(r'^clientfixeddepositsprofile/(?P<fixed_deposit_id>\d+)/$',
        client_fixed_deposits_profile, name="clientfixeddepositsprofile"),
    url(r'^viewclientfixeddeposits/$',
        view_client_fixed_deposits, name="viewclientfixeddeposits"),
    url(r'^viewdaybook/$', view_day_book, name="viewdaybook"),
    url(r'^viewparticularclientfixeddeposits/(?P<client_id>\d+)/$',
        view_particular_client_fixed_deposits,
        name="viewparticularclientfixeddeposits"),
    url(r'^payslip/$', pay_slip, name="payslip"),
    url(r'^grouploanaccountslist/(?P<group_id>\d+)/$',
        view_group_loanslist, name="grouploanaccountslist"),
    url(r'^clientloanaccountslist/(?P<client_id>\d+)/$',
        view_client_loanslist, name="clientloanaccountslist"),
    url(r'^paymentslist/$', payments_list, name="paymentslist"),
    url(r'^recurringdeposits/$', recurring_deposits, name="recurringdeposits"),
    url(r'^clientrecurringdepositsprofile/(?P<recurring_deposit_id>\d+)/$',
        client_recurring_deposits_profile,
        name="clientrecurringdepositsprofile"),
    url(r'^viewclientrecurringdeposits/$', view_client_recurring_deposits,
        name="viewclientrecurringdeposits"),
    url(r'^viewparticularclientrecurringdeposits/(?P<client_id>\d+)/$',
        view_particular_client_recurring_deposits,
        name="viewparticularclientrecurringdeposits"),
    url(r'^clientledgercsvdownload/(?P<client_id>\d+)/$',
        clientledger_csvdownload, name="clientledgercsvdownload"),
    url(r'^clientledgerexceldownload/(?P<client_id>\d+)/$',
        clientledger_exceldownload, name="clientledgerexceldownload"),
    url(r'^clientledgerpdfdownload/(?P<client_id>\d+)/$',
        clientledger_pdfdownload, name="clientledgerpdfdownload"),
    url(r'^generalledgerpdfdownload/$', general_ledger_pdfdownload,
        name="generalledgerpdfdownload"),
    url(r'^daybookpdfdownload/(?P<date>\d{4}-\d{2}-\d{2})/$',
        daybook_pdfdownload, name="daybookpdfdownload"),
    url(r'^userchangepassword/(?P<user_id>\d+)/$', user_change_password,
        name="userchangepassword"),
    url(r'^getmemberloanaccounts/$', getmember_loanaccounts,
        name="getmemberloanaccounts"),
    url(r'^getloandemands/$', getloan_demands, name="getloandemands"),
]