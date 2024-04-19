# Generated by Django 3.1.2 on 2020-10-12 09:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    # do a collation change sql script in the intial migration
    collation_sql = 'ALTER DATABASE ' + \
         settings.DATABASES['default']['NAME'] + ' CHARACTER SET ' + \
              settings.DATABASES['default']['OPTIONS']['charset'] + ' COLLATE ' + \
                   settings.DB_COLLATION['CORRECT'] + ';'
    
    # reverse migration for collation
    reverse_collaction_sql = 'ALTER DATABASE ' + \
         settings.DATABASES['default']['NAME'] + ' CHARACTER SET ' + \
              settings.DATABASES['default']['OPTIONS']['charset'] + ' COLLATE ' + \
                   settings.DB_COLLATION['DEFAULT_BUT_WRONG'] + ';'

    operations = [
        migrations.RunSQL(
            sql=[(collation_sql)],
            reverse_sql=[(reverse_collaction_sql)],
        ),


        migrations.CreateModel(
            name='BioLib',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_name', models.TextField(null=True)),
                ('author_name', models.TextField(null=True)),
                ('author_username', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('biolib', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='elixir.biolib')),
            ],
        ),
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
                ('email', models.TextField(blank=True, null=True)),
                ('url', models.TextField(blank=True, null=True)),
                ('orcidid', models.TextField(blank=True, null=True)),
                ('gridid', models.TextField(blank=True, null=True)),
                ('rorid', models.TextField(blank=True, null=True)),
                ('fundrefid', models.TextField(blank=True, null=True)),
                ('typeEntity', models.TextField(blank=True, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('additionDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uri', models.TextField(blank=True, null=True)),
                ('term', models.TextField(blank=True, null=True)),
                ('additionDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Documentation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField()),
                ('type_old', models.TextField()),
                ('note', models.TextField(blank=True, null=True)),
                ('additionDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('title', models.TextField(blank=True, null=True)),
                ('sub_title', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EditPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.TextField(default='private')),
            ],
        ),
        migrations.CreateModel(
            name='ElixirInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.TextField(blank=True, null=True)),
                ('node', models.TextField(blank=True, null=True)),
                ('additionDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Function',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(blank=True, null=True)),
                ('cmd', models.TextField(blank=True, max_length=100, null=True)),
                ('additionDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='IssueState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='IssueType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('weight', models.FloatField(blank=True, null=True)),
                ('attribute', models.TextField(blank=True, null=True)),
                ('field_name', models.TextField(blank=True, null=True)),
                ('field_value', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField()),
                ('type_old', models.TextField()),
                ('note', models.TextField(blank=True, null=True)),
                ('additionDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ontology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
                ('data', models.TextField(blank=True, null=True)),
                ('additionDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pmcid', models.TextField(blank=True, null=True)),
                ('pmid', models.TextField(blank=True, null=True)),
                ('doi', models.TextField(blank=True, null=True)),
                ('type_old', models.TextField(blank=True, null=True)),
                ('version', models.TextField(blank=True, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('additionDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PublicationMetadata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(blank=True, null=True)),
                ('title', models.TextField(blank=True, null=True)),
                ('journal', models.TextField(blank=True, null=True)),
                ('abstract', models.TextField(blank=True, null=True)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('citationCount', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('biotoolsID', models.CharField(max_length=100)),
                ('biotoolsCURIE', models.CharField(max_length=109)),
                ('name', models.TextField()),
                ('versionId', models.CharField(default='none', max_length=100, null=True)),
                ('homepage', models.TextField()),
                ('description', models.TextField()),
                ('short_description', models.TextField(blank=True, null=True)),
                ('canonicalID', models.TextField(blank=True, null=True)),
                ('issue_score', models.FloatField(blank=True, null=True)),
                ('version_hash', models.TextField(blank=True, null=True)),
                ('visibility', models.IntegerField(choices=[(0, 'NO'), (1, 'YES')], default=1)),
                ('latest', models.IntegerField(choices=[(0, 'NO'), (1, 'YES')], default=1)),
                ('was_id_validated', models.IntegerField(choices=[(0, 'NO'), (1, 'YES')], default=0)),
                ('homepage_status', models.IntegerField(choices=[(0, 'UP'), (1, 'DOWN'), (2, 'DEAD')], default=0)),
                ('elixir_badge', models.IntegerField(choices=[(0, 'None'), (1, 'EDD'), (2, 'CDR'), (3, 'EDD,CDR'), (4, 'RIR'), (5, 'EDD,RIR'), (6, 'CDR,RIR'), (7, 'EDD,CDR,RIR')], default=0)),
                ('confidence_flag', models.TextField(blank=True, null=True)),
                ('cost', models.TextField(blank=True, null=True)),
                ('accessibility', models.TextField(blank=True, null=True)),
                ('maturity', models.TextField(blank=True, null=True)),
                ('license', models.TextField(blank=True, null=True)),
                ('additionDate', models.DateTimeField(blank=True, null=True)),
                ('lastUpdate', models.DateTimeField(auto_now=True)),
                ('availability', models.TextField(blank=True, null=True)),
                ('downtime', models.TextField(blank=True, null=True)),
                ('community', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='elixir.community')),
                ('editPermission', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='elixir.editpermission')),
                ('elixirInfo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='elixir.elixirinfo')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resource', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StatsData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('data', jsonfield.fields.JSONField(blank=True, null=True)),
                ('totalEntries', models.IntegerField(default=0)),
                ('creditAffiliationCount', models.IntegerField()),
                ('edamAnnotationsCount', models.IntegerField()),
                ('formatAnnotationsCount', models.IntegerField()),
                ('functionAnnotationsCount', models.IntegerField()),
                ('topicAnnotationsCount', models.IntegerField()),
                ('dataTypeAnnotationsCount', models.IntegerField()),
                ('nameAnnotationCount', models.IntegerField(default=0)),
                ('uniqueIDAnnotationCount', models.IntegerField(default=0)),
                ('topicAnnotationCount', models.IntegerField(default=0)),
                ('operatingSystemAnnotationCount', models.IntegerField(default=0)),
                ('codeAvailabilityAnnotationCount', models.IntegerField(default=0)),
                ('operationAnnotationCount', models.IntegerField(default=0)),
                ('descriptionAnnotationCount', models.IntegerField(default=0)),
                ('downloadsAnnotationCount', models.IntegerField(default=0)),
                ('dataFormatsAnnotationCount', models.IntegerField(default=0)),
                ('accessibilityAnnotationCount', models.IntegerField(default=0)),
                ('toolTypeAnnotationCount', models.IntegerField(default=0)),
                ('documentationAnnotationCount', models.IntegerField(default=0)),
                ('inputOutputAnnotationCount', models.IntegerField(default=0)),
                ('communityAnnotationCount', models.IntegerField(default=0)),
                ('contactAnnotationCount', models.IntegerField(default=0)),
                ('homepageAnnotationCount', models.IntegerField(default=0)),
                ('publicationAnnotationCount', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Workflow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('biotoolsID', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('sourceURL', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(height_field='image_height', upload_to='workflows/', width_field='image_width')),
                ('image_width', models.IntegerField(default=0)),
                ('image_height', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='WorkflowAnnotation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startX', models.FloatField()),
                ('startY', models.FloatField()),
                ('endX', models.FloatField()),
                ('endY', models.FloatField()),
                ('title', models.TextField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('edam_term', models.TextField(blank=True, null=True)),
                ('edam_uri', models.TextField(blank=True, null=True)),
                ('url', models.TextField(blank=True, null=True)),
                ('workflow', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='annotations', to='elixir.workflow')),
            ],
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.TextField(blank=True, null=True)),
                ('additionDate', models.DateTimeField(auto_now_add=True)),
                ('resource', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='version', to='elixir.resource')),
            ],
        ),
        migrations.CreateModel(
            name='Uses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
                ('homepage', models.TextField(blank=True, null=True)),
                ('version', models.TextField(blank=True, null=True)),
                ('additionDate', models.DateTimeField(auto_now_add=True)),
                ('resource', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='uses', to='elixir.resource')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uri', models.TextField(blank=True, null=True)),
                ('term', models.TextField(blank=True, null=True)),
                ('additionDate', models.DateTimeField(auto_now_add=True)),
                ('resource', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='topic', to='elixir.resource')),
            ],
        ),
        migrations.CreateModel(
            name='ToolType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
                ('additionDate', models.DateTimeField(auto_now_add=True)),
                ('resource', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='toolType', to='elixir.resource')),
            ],
        ),
        migrations.CreateModel(
            name='SearchTermLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=32, null=True)),
                ('term', models.CharField(blank=True, max_length=32, null=True)),
            ],
            options={
                'unique_together': {('name', 'term')},
            },
        ),
        migrations.CreateModel(
            name='SearchQueryLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('terms', models.ManyToManyField(related_name='queries', to='elixir.SearchTermLog')),
            ],
        ),
        migrations.CreateModel(
            name='ResourceRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requestId', models.CharField(max_length=50)),
                ('type', models.TextField(blank=True, null=True)),
                ('completed', models.BooleanField(default=False)),
                ('accepted', models.BooleanField(default=False)),
                ('completedBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('resource', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='elixir.resource')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='requests', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('biotoolsID', models.CharField(max_length=100)),
                ('type', models.TextField()),
                ('additionDate', models.DateTimeField(auto_now_add=True)),
                ('resource', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='relation', to='elixir.resource')),
            ],
        ),
        migrations.CreateModel(
            name='PublicationType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.TextField(blank=True, null=True)),
                ('additionDate', models.DateTimeField(auto_now_add=True)),
                ('publication', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='type', to='elixir.publication')),
            ],
        ),
        migrations.CreateModel(
            name='PublicationAuthor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
                ('metadata', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='authors', to='elixir.publicationmetadata')),
            ],
        ),
        migrations.AddField(
            model_name='publication',
            name='metadata',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='publication', to='elixir.publicationmetadata'),
        ),
        migrations.AddField(
            model_name='publication',
            name='resource',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='publication', to='elixir.resource'),
        ),
        migrations.CreateModel(
            name='Output',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('additionDate', models.DateTimeField(auto_now_add=True)),
                ('data', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='elixir.data')),
                ('function', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='output', to='elixir.function')),
            ],
        ),
        migrations.CreateModel(
            name='OtherID',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=1000)),
                ('type', models.TextField(blank=True, null=True)),
                ('version', models.TextField(blank=True, null=True)),
                ('additionDate', models.DateTimeField(auto_now_add=True, null=True)),
                ('resource', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='otherID', to='elixir.resource')),
            ],
        ),
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uri', models.TextField(blank=True, null=True)),
                ('term', models.TextField(blank=True, null=True)),
                ('additionDate', models.DateTimeField(auto_now_add=True)),
                ('function', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='operation', to='elixir.function')),
            ],
        ),
        migrations.CreateModel(
            name='OperatingSystem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
                ('additionDate', models.DateTimeField(auto_now_add=True)),
                ('resource', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='operatingSystem', to='elixir.resource')),
            ],
        ),
        migrations.CreateModel(
            name='LinkType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.TextField(blank=True, null=True)),
                ('additionDate', models.DateTimeField(auto_now_add=True)),
                ('link', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='type', to='elixir.link')),
            ],
        ),
        migrations.AddField(
            model_name='link',
            name='resource',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='link', to='elixir.resource'),
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
                ('additionDate', models.DateTimeField(auto_now_add=True)),
                ('resource', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='language', to='elixir.resource')),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_name', models.TextField(blank=True, null=True)),
                ('field_value', models.TextField(blank=True, null=True)),
                ('resource_biotoolsID', models.TextField(blank=True, null=True)),
                ('resource_versionId', models.TextField(blank=True, null=True)),
                ('resolution_date', models.DateTimeField(blank=True, null=True)),
                ('resolution_actor', models.CharField(blank=True, max_length=32, null=True)),
                ('creation_actor', models.TextField(blank=True, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('additionDate', models.DateTimeField(auto_now_add=True)),
                ('issue_state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elixir.issuestate')),
                ('issue_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elixir.issuetype')),
            ],
        ),
        migrations.CreateModel(
            name='Input',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('additionDate', models.DateTimeField(auto_now_add=True)),
                ('data', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='elixir.data')),
                ('function', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='input', to='elixir.function')),
            ],
        ),
        migrations.AddField(
            model_name='function',
            name='resource',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='function', to='elixir.resource'),
        ),
        migrations.CreateModel(
            name='Format',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uri', models.TextField(blank=True, null=True)),
                ('term', models.TextField(blank=True, null=True)),
                ('additionDate', models.DateTimeField(auto_now_add=True)),
                ('input', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='format', to='elixir.input')),
                ('output', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='format', to='elixir.output')),
            ],
        ),
        migrations.CreateModel(
            name='ElixirPlatform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('elixirPlatform', models.TextField(null=True)),
                ('additionDate', models.DateTimeField(auto_now_add=True)),
                ('resource', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='elixirPlatform', to='elixir.resource')),
            ],
        ),
        migrations.CreateModel(
            name='ElixirNode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('elixirNode', models.TextField(null=True)),
                ('additionDate', models.DateTimeField(auto_now_add=True)),
                ('resource', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='elixirNode', to='elixir.resource')),
            ],
        ),
        migrations.CreateModel(
            name='ElixirCommunity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('elixirCommunity', models.TextField(null=True)),
                ('additionDate', models.DateTimeField(auto_now_add=True)),
                ('resource', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='elixirCommunity', to='elixir.resource')),
            ],
        ),
        migrations.CreateModel(
            name='EditPermissionAuthor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('editPermissions', models.ManyToManyField(related_name='authors', to='elixir.EditPermission')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Download',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField()),
                ('type', models.TextField()),
                ('note', models.TextField(blank=True, null=True)),
                ('version', models.TextField(blank=True, null=True)),
                ('cmd', models.TextField(blank=True, max_length=100, null=True)),
                ('additionDate', models.DateTimeField(auto_now_add=True)),
                ('resource', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='download', to='elixir.resource')),
            ],
        ),
        migrations.CreateModel(
            name='DomainResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('version', models.TextField(blank=True, null=True)),
                ('biotoolsID', models.TextField()),
                ('versionId', models.TextField()),
                ('additionDate', models.DateTimeField(auto_now_add=True)),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elixir.domain')),
            ],
        ),
        migrations.CreateModel(
            name='DocumentationType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.TextField(blank=True, null=True)),
                ('additionDate', models.DateTimeField(auto_now_add=True)),
                ('documentation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='type', to='elixir.documentation')),
            ],
        ),
        migrations.AddField(
            model_name='documentation',
            name='resource',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='documentation', to='elixir.resource'),
        ),
        migrations.CreateModel(
            name='CreditTypeRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeRole', models.TextField(blank=True, null=True)),
                ('additionDate', models.DateTimeField(auto_now_add=True)),
                ('credit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='typeRole', to='elixir.credit')),
            ],
        ),
        migrations.AddField(
            model_name='credit',
            name='resource',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='credit', to='elixir.resource'),
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.TextField(blank=True, null=True)),
                ('name', models.TextField(blank=True, null=True)),
                ('tel', models.TextField(blank=True, null=True)),
                ('url', models.TextField(blank=True, null=True)),
                ('additionDate', models.DateTimeField(auto_now_add=True)),
                ('resource', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contact', to='elixir.resource')),
            ],
        ),
        migrations.CreateModel(
            name='CollectionID',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
                ('additionDate', models.DateTimeField(auto_now_add=True)),
                ('resource', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='collectionID', to='elixir.resource')),
            ],
        ),
        migrations.CreateModel(
            name='Accessibility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
                ('additionDate', models.DateTimeField(auto_now_add=True)),
                ('resource', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='accessibility_old', to='elixir.resource')),
            ],
        ),
    ]
