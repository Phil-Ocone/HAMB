import unittest

from cocore.config import Config

from hambot.ham_run_utility import TestEngine, HandlerEngine, json_serial

import datetime



class TestHamrun(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        conf = Config()

        test_conf = dict()
        test_conf['label'] = 'this is a test'
        test_conf['conn_a'] = 'life'
        test_conf['conn_b'] = 'cosmo'
        test_conf['script_a'] = '''
        if object_id('tempdb..##dmr_watch_zero_eqx11') is not null
                drop Table ##dmr_watch_zero_eqx11;
                select summarydate,
                case when company_id in (1,4,5) then 'Equinox' else company_name end company_name,
                case when company_id in (1,4,5) then 1 else company_id end company_id,
                bizactionsid,
                bizaction_display_Name,
                count(distinct Facilityid)Total_Clubs,
                sum(Zero_Daily)Zero_Daily,
                sum(daily) as daily,
                case
                  when (summarydate between concat(year(summarydate), '/11/22') and concat(year(summarydate), '/11/28')) then 0.9
                  when (summarydate between concat(year(summarydate), '/12/24') and concat(year(summarydate), '/12/26')) then 0.9
                  else 0.75
                end as threshold
                into ##dmr_watch_zero_eqx11
                from
                (select summarydate,Facilityid,company_name,  company_id, bizactionsid, k.bizaction_display_Name,
                case when sum(isnull(daily,0)) = 0 then 1 else 0 end Zero_Daily,
                sum(daily) as daily
                from dbo.eqx_tblDailyManagementReport
                 join mstr.d_management_kpi k on bizactionsid = k.nk_management_kpi_id
                 join mstr.d_facility f on f.facility_code = facilityid and is_last_transaction_flag='y'
                where summarydate = cast(convert(varchar(12),getdate(),101) as datetime) -1
                 and company_id in (1,4,5)
                 and bizactionsid in (1,5,6,7,8,9,14,15,16)
                group by summarydate, Facilityid,company_name, company_id, bizactionsid, k.bizaction_display_Name )a
                group by summarydate,
                case when company_id in (1,4,5) then 'Equinox' else company_name end,
                case when company_id in (1,4,5) then 1 else company_id end,
                bizactionsid, bizaction_display_Name;

                select count(1) FROM ##dmr_watch_zero_eqx11
                where cast(Zero_Daily as float)/cast(Total_Clubs as float) > threshold
                and bizactionsid =1 and company_id in (1,4,5)
        '''
        test_conf['script_b'] = '''
            CREATE TEMPORARY TABLE temp_sql_count
                AS
                SELECT COUNT(*) as cache_count
                FROM edw_landing.cache_trainer_performance;

                select count(1) FROM temp_sql_count;
        '''
        test_conf['pct_diff'] = True
        test_conf['heartbeat'] = True
        cls.TestEngine = TestEngine()
        cls.HandlerEngine = HandlerEngine()

    def test_run(self):
        result = self.TestEngine.run('sample')
        self.HandlerEngine.run('sample', result)

    def test_json_serial(self):
        json_serial(datetime.datetime(2015, 2, 1, 15, 16, 17, 345))
