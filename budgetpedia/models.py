# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AcctDim(models.Model):
    acc_id = models.AutoField(db_column='ACC_ID', primary_key=True)  # Field name made lowercase.
    acc_name = models.CharField(db_column='ACC_NAME', max_length=100)  # Field name made lowercase.
    acc_desc = models.CharField(db_column='ACC_DESC', max_length=100)  # Field name made lowercase.
    acc_code = models.CharField(db_column='ACC_CODE', max_length=20)  # Field name made lowercase.
    acc_common_identifier = models.CharField(db_column='ACC_COMMON_IDENTIFIER', max_length=50, blank=True, null=True)  # Field name made lowercase.
    acc_type = models.CharField(db_column='ACC_TYPE', max_length=50)  # Field name made lowercase.

    class Meta:
        db_table = 'ACCT_DIM'


class AcctPeroidDim(models.Model):
    per_id = models.IntegerField(db_column='PER_ID', primary_key=True)  # Field name made lowercase.
    per_number = models.IntegerField(db_column='PER_NUMBER', blank=True, null=True)  # Field name made lowercase.
    per_desc = models.CharField(db_column='PER_DESC', max_length=100)  # Field name made lowercase.
    per_fiscal_year = models.IntegerField(db_column='PER_FISCAL_YEAR')  # Field name made lowercase.
    per_type = models.CharField(db_column='PER_TYPE', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'ACCT_PEROID_DIM'


class BudgetFact(models.Model):
    bf_mvr_id = models.IntegerField(db_column='BF_MVR_ID', primary_key=True)  # Field name made lowercase.
    bf_rep_id = models.IntegerField(db_column='BF_REP_ID')  # Field name made lowercase.
    bf_dom_id = models.CharField(db_column='BF_DOM_ID', max_length=40)  # Field name made lowercase.
    bf_per_id = models.IntegerField(db_column='BF_PER_ID')  # Field name made lowercase.
    bf_acc_id = models.IntegerField(db_column='BF_ACC_ID')  # Field name made lowercase.
    bf_amount = models.IntegerField(db_column='BF_AMOUNT')  # Field name made lowercase.

    class Meta:
        db_table = 'BUDGET_FACT'
        unique_together = (('bf_mvr_id', 'bf_rep_id', 'bf_dom_id', 'bf_per_id', 'bf_acc_id'),)


class ModelVersionDim(models.Model):
    mvr_id = models.IntegerField(db_column='MVR_ID', primary_key=True)  # Field name made lowercase.
    mvr_version = models.CharField(db_column='MVR_VERSION', max_length=50)  # Field name made lowercase.
    mvr_type = models.CharField(db_column='MVR_TYPE', max_length=100)  # Field name made lowercase.
    mvr_approval_date = models.DateField(db_column='MVR_APPROVAL_DATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'MODEL_VERSION_DIM'


class RepTypeDim(models.Model):
    rep_id = models.IntegerField(db_column='REP_ID', primary_key=True)  # Field name made lowercase.
    rep_type = models.CharField(db_column='REP_TYPE', max_length=50)  # Field name made lowercase.
    rep_name = models.CharField(db_column='REP_NAME', max_length=100)  # Field name made lowercase.
    rep_category = models.CharField(db_column='REP_CATEGORY', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'REP_TYPE_DIM'


class BudgetAmountRevenues(models.Model):
    tax = models.ForeignKey('Taxonomy', models.DO_NOTHING, primary_key=True)
    trans_type = models.ForeignKey('BudgetTransformationType', models.DO_NOTHING)
    source_peroid = models.CharField(max_length=10)
    tax_peroid = models.CharField(max_length=10)
    domain_code = models.CharField(max_length=20)
    type = models.CharField(max_length=1, blank=True, null=True)
    revenues_amount = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True)

    class Meta:
        db_table = 'budget_amount_revenues'
        unique_together = (('tax', 'domain_code', 'source_peroid'),)


class BudgetTransformationType(models.Model):
    trans_type_id = models.IntegerField(primary_key=True)
    owner = models.CharField(max_length=10)
    description = models.CharField(max_length=100)

    class Meta:
        db_table = 'budget_transformation_type'


class DomainGroup(models.Model):
    id = models.CharField(max_length=40, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'domain_group'


class DomainGroupMembers(models.Model):
    dg_id = models.CharField(max_length=40, primary_key = True)
    domain_id = models.CharField(max_length=100)

    class Meta:
        db_table = 'domain_group_members'


class DomainIdentifier(models.Model):
    id = models.CharField(max_length=40, primary_key=True)
    code = models.CharField(unique=True, max_length=50, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        db_table = 'domain_identifier'


class FragmentGraph(models.Model):
    id = models.CharField(max_length=40, primary_key=True)
    root_to_id = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        db_table = 'fragment_graph'


class FragmentGraphDomain(models.Model):
    id = models.CharField(max_length=40, primary_key=True)
    code = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        db_table = 'fragment_graph_domain'


class FragmentGraphEdge(models.Model):
    fg_id = models.CharField(max_length=40, blank=True, null=True)
    from_id = models.CharField(max_length=40, blank=True, null=True)
    to_id = models.CharField(max_length=40, blank=True, null=True)
    hops = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'fragment_graph_edge'


class Taxonomy(models.Model):
    tax_id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=100)
    version = models.IntegerField()
    tax_peroid = models.CharField(max_length=100, blank=True, null=True)
    originator = models.CharField(max_length=50, blank=True, null=True)
    coverage = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=20)
    normalised = models.IntegerField()

    class Meta:
        db_table = 'taxonomy'


class TaxonomyMapping(models.Model):
    tax_map_id = models.IntegerField(primary_key=True)
    from_tax = models.ForeignKey(Taxonomy, models.DO_NOTHING)
    to_tax = models.ForeignKey(Taxonomy, models.DO_NOTHING)
    description = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'taxonomy_mapping'


class TaxonomyMappingRule(models.Model):
    tax_map_rule_id = models.AutoField(primary_key=True)
    tax_map = models.ForeignKey(TaxonomyMapping, models.DO_NOTHING)
    from_domain_code = models.ForeignKey(DomainIdentifier, models.DO_NOTHING, db_column='from_domain_code')
    from_weighting = models.DecimalField(max_digits=3, decimal_places=2)
    to_domain_code = models.ForeignKey(DomainIdentifier, models.DO_NOTHING, db_column='to_domain_code')
    is_transform = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        db_table = 'taxonomy_mapping_rule'
