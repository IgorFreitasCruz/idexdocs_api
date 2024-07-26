"""First migration

Revision ID: d1ea98482c76
Revises: 
Create Date: 2024-06-17 21:03:20.515328

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = 'd1ea98482c76'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('atleta',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('data_nascimento', sa.Date(), nullable=False),
    sa.Column('data_criacao', sa.DateTime(), nullable=False),
    sa.Column('data_atualizado', sa.DateTime(), nullable=True),
    sa.Column('ativo', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('contratotipo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tipo', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('data_criacao', sa.DateTime(), nullable=False),
    sa.Column('data_atualizado', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('perfil',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('data_criacao', sa.DateTime(), nullable=False),
    sa.Column('data_atualizado', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('permissao',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('descricao', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('data_criacao', sa.DateTime(), nullable=False),
    sa.Column('data_atualizado', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('posicao',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('data_criacao', sa.DateTime(), nullable=False),
    sa.Column('data_atualizado', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('descricao', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('data_criacao', sa.DateTime(), nullable=False),
    sa.Column('data_atualizado', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('usuariotipo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tipo', sa.Enum('admin', 'treinador', 'externo', name='usuariotipotypes'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('atletaavatar',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('blob_url', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('data_criacao', sa.DateTime(), nullable=False),
    sa.Column('data_atualizado', sa.DateTime(), nullable=True),
    sa.Column('atleta_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['atleta_id'], ['atleta.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('atletaimagens',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('blob_url', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('descricao', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('data_criacao', sa.DateTime(), nullable=False),
    sa.Column('data_atualizado', sa.DateTime(), nullable=True),
    sa.Column('atleta_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['atleta_id'], ['atleta.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('atletaposicao',
    sa.Column('atleta_id', sa.Integer(), nullable=False),
    sa.Column('posicao_id', sa.Integer(), nullable=False),
    sa.Column('preferencia', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('data_criacao', sa.DateTime(), nullable=False),
    sa.Column('data_atualizado', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['atleta_id'], ['atleta.id'], ),
    sa.ForeignKeyConstraint(['posicao_id'], ['posicao.id'], ),
    sa.PrimaryKeyConstraint('atleta_id', 'posicao_id')
    )
    op.create_table('atletavideos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('blob_url', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('tipo', sa.Enum('video', 'youtube', name='atletavideotypes'), nullable=True),
    sa.Column('descricao', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('data_criacao', sa.DateTime(), nullable=False),
    sa.Column('data_atualizado', sa.DateTime(), nullable=True),
    sa.Column('atleta_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['atleta_id'], ['atleta.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('caracteristica',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('data_criacao', sa.DateTime(), nullable=False),
    sa.Column('data_atualizado', sa.DateTime(), nullable=True),
    sa.Column('perfil_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['perfil_id'], ['perfil.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('caracteristicaatacante',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('estatura_fis', sa.Integer(), nullable=False),
    sa.Column('velocidade_fis', sa.Integer(), nullable=False),
    sa.Column('um_contra_um_ofensivo_fis', sa.Integer(), nullable=False),
    sa.Column('desmarques_fis', sa.Integer(), nullable=False),
    sa.Column('controle_bola_fis', sa.Integer(), nullable=False),
    sa.Column('cruzamentos_fis', sa.Integer(), nullable=False),
    sa.Column('finalizacao_fis', sa.Integer(), nullable=False),
    sa.Column('visao_espacial_tec', sa.Integer(), nullable=False),
    sa.Column('dominio_orientado_tec', sa.Integer(), nullable=False),
    sa.Column('dribles_em_diagonal_tec', sa.Integer(), nullable=False),
    sa.Column('leitura_jogo_tec', sa.Integer(), nullable=False),
    sa.Column('reacao_pos_perda_tec', sa.Integer(), nullable=False),
    sa.Column('criatividade_psi', sa.Integer(), nullable=False),
    sa.Column('capacidade_decisao_psi', sa.Integer(), nullable=False),
    sa.Column('inteligencia_tatica_psi', sa.Integer(), nullable=False),
    sa.Column('competitividade_psi', sa.Integer(), nullable=False),
    sa.Column('data_avaliacao', sa.Date(), nullable=True),
    sa.Column('data_criacao', sa.DateTime(), nullable=False),
    sa.Column('data_atualizado', sa.DateTime(), nullable=True),
    sa.Column('atleta_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['atleta_id'], ['atleta.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('caracteristicafisica',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('estatura', sa.Float(), nullable=True),
    sa.Column('envergadura', sa.Float(), nullable=True),
    sa.Column('peso', sa.Float(), nullable=True),
    sa.Column('percentual_gordura', sa.Float(), nullable=True),
    sa.Column('data_avaliacao', sa.Date(), nullable=True),
    sa.Column('data_criacao', sa.DateTime(), nullable=False),
    sa.Column('data_atualizado', sa.DateTime(), nullable=True),
    sa.Column('atleta_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['atleta_id'], ['atleta.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('caracteristicagoleiro',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('perfil_fis', sa.Integer(), nullable=False),
    sa.Column('maturacao_fis', sa.Integer(), nullable=False),
    sa.Column('agilidade_fis', sa.Integer(), nullable=False),
    sa.Column('velocidade_membros_superiores_fis', sa.Integer(), nullable=False),
    sa.Column('flexibilidade_fis', sa.Integer(), nullable=False),
    sa.Column('posicionamento_fis', sa.Integer(), nullable=False),
    sa.Column('leitura_jogo_tec', sa.Integer(), nullable=False),
    sa.Column('jogo_com_pes_tec', sa.Integer(), nullable=False),
    sa.Column('organizacao_da_defesa_tec', sa.Integer(), nullable=False),
    sa.Column('dominio_coberturas_e_saidas_tec', sa.Integer(), nullable=False),
    sa.Column('lideranca_psi', sa.Integer(), nullable=False),
    sa.Column('coragem_psi', sa.Integer(), nullable=False),
    sa.Column('concentracao_psi', sa.Integer(), nullable=False),
    sa.Column('controle_estresse_psi', sa.Integer(), nullable=False),
    sa.Column('data_avaliacao', sa.Date(), nullable=True),
    sa.Column('data_criacao', sa.DateTime(), nullable=False),
    sa.Column('data_atualizado', sa.DateTime(), nullable=True),
    sa.Column('atleta_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['atleta_id'], ['atleta.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('caracteristicalateral',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('estatura_fis', sa.Integer(), nullable=False),
    sa.Column('velocidade_fis', sa.Integer(), nullable=False),
    sa.Column('passe_curto_fis', sa.Integer(), nullable=False),
    sa.Column('passe_longo_fis', sa.Integer(), nullable=False),
    sa.Column('capacidade_aerobia_fis', sa.Integer(), nullable=False),
    sa.Column('fechemanento_defensivo_fis', sa.Integer(), nullable=False),
    sa.Column('leitura_jogo_tec', sa.Integer(), nullable=False),
    sa.Column('participacao_ofensiva_tec', sa.Integer(), nullable=False),
    sa.Column('cruzamento_tec', sa.Integer(), nullable=False),
    sa.Column('jogo_aereo_tec', sa.Integer(), nullable=False),
    sa.Column('conducao_bola_tec', sa.Integer(), nullable=False),
    sa.Column('lideranca_psi', sa.Integer(), nullable=False),
    sa.Column('confianca_psi', sa.Integer(), nullable=False),
    sa.Column('inteligencia_tatica_psi', sa.Integer(), nullable=False),
    sa.Column('competitividade_psi', sa.Integer(), nullable=False),
    sa.Column('data_avaliacao', sa.Date(), nullable=True),
    sa.Column('data_criacao', sa.DateTime(), nullable=False),
    sa.Column('data_atualizado', sa.DateTime(), nullable=True),
    sa.Column('atleta_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['atleta_id'], ['atleta.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('caracteristicameia',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('estatura_fis', sa.Integer(), nullable=False),
    sa.Column('velocidade_fis', sa.Integer(), nullable=False),
    sa.Column('leitura_jogo_fis', sa.Integer(), nullable=False),
    sa.Column('desmarques_fis', sa.Integer(), nullable=False),
    sa.Column('controle_bola_fis', sa.Integer(), nullable=False),
    sa.Column('capacidade_aerobia_fis', sa.Integer(), nullable=False),
    sa.Column('finalizacao_fis', sa.Integer(), nullable=False),
    sa.Column('visao_espacial_tec', sa.Integer(), nullable=False),
    sa.Column('dominio_orientado_tec', sa.Integer(), nullable=False),
    sa.Column('dribles_tec', sa.Integer(), nullable=False),
    sa.Column('organizacao_acao_ofensica_tec', sa.Integer(), nullable=False),
    sa.Column('pisada_na_area_para_finalizar_tec', sa.Integer(), nullable=False),
    sa.Column('criatividade_psi', sa.Integer(), nullable=False),
    sa.Column('capacidade_decisao_psi', sa.Integer(), nullable=False),
    sa.Column('confianca_psi', sa.Integer(), nullable=False),
    sa.Column('inteligencia_tatica_psi', sa.Integer(), nullable=False),
    sa.Column('competitividade_psi', sa.Integer(), nullable=False),
    sa.Column('data_avaliacao', sa.Date(), nullable=True),
    sa.Column('data_criacao', sa.DateTime(), nullable=False),
    sa.Column('data_atualizado', sa.DateTime(), nullable=True),
    sa.Column('atleta_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['atleta_id'], ['atleta.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('caracteristicavolante',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('estatura_fis', sa.Integer(), nullable=False),
    sa.Column('forca_fis', sa.Integer(), nullable=False),
    sa.Column('passe_curto_fis', sa.Integer(), nullable=False),
    sa.Column('capacidade_aerobia_fis', sa.Integer(), nullable=False),
    sa.Column('dinamica_fis', sa.Integer(), nullable=False),
    sa.Column('visao_espacial_fis', sa.Integer(), nullable=False),
    sa.Column('leitura_jogo_tec', sa.Integer(), nullable=False),
    sa.Column('dominio_orientado_tec', sa.Integer(), nullable=False),
    sa.Column('jogo_aereo_ofensivo_tec', sa.Integer(), nullable=False),
    sa.Column('passes_verticais_tec', sa.Integer(), nullable=False),
    sa.Column('finalizacao_media_distancia_tec', sa.Integer(), nullable=False),
    sa.Column('lideranca_psi', sa.Integer(), nullable=False),
    sa.Column('confianca_psi', sa.Integer(), nullable=False),
    sa.Column('inteligencia_tatica_psi', sa.Integer(), nullable=False),
    sa.Column('competitividade_psi', sa.Integer(), nullable=False),
    sa.Column('data_avaliacao', sa.Date(), nullable=True),
    sa.Column('data_criacao', sa.DateTime(), nullable=False),
    sa.Column('data_atualizado', sa.DateTime(), nullable=True),
    sa.Column('atleta_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['atleta_id'], ['atleta.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('caracteristicazagueiro',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('estatura_fis', sa.Integer(), nullable=False),
    sa.Column('força_fis', sa.Integer(), nullable=False),
    sa.Column('passe_curto_fis', sa.Integer(), nullable=False),
    sa.Column('passe_longo_fis', sa.Integer(), nullable=False),
    sa.Column('jogo_aereo_fis', sa.Integer(), nullable=False),
    sa.Column('confronto_defensivo_fis', sa.Integer(), nullable=False),
    sa.Column('leitura_jogo_tec', sa.Integer(), nullable=False),
    sa.Column('ambidestria_tec', sa.Integer(), nullable=False),
    sa.Column('participacao_ofensica_tec', sa.Integer(), nullable=False),
    sa.Column('cabeceio_ofensivo_tec', sa.Integer(), nullable=False),
    sa.Column('passe_entre_linhas_tec', sa.Integer(), nullable=False),
    sa.Column('lideranca_psi', sa.Integer(), nullable=False),
    sa.Column('confianca_psi', sa.Integer(), nullable=False),
    sa.Column('inteligencia_tatica_psi', sa.Integer(), nullable=False),
    sa.Column('competitividade_psi', sa.Integer(), nullable=False),
    sa.Column('data_avaliacao', sa.Date(), nullable=True),
    sa.Column('data_criacao', sa.DateTime(), nullable=False),
    sa.Column('data_atualizado', sa.DateTime(), nullable=True),
    sa.Column('atleta_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['atleta_id'], ['atleta.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('contratosubtipo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('contrato_tipo_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['contrato_tipo_id'], ['contratotipo.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('historicoclube',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('data_inicio', sa.Date(), nullable=False),
    sa.Column('data_fim', sa.Date(), nullable=False),
    sa.Column('clube_atual', sa.Boolean(), nullable=False),
    sa.Column('data_criacao', sa.DateTime(), nullable=False),
    sa.Column('data_atualizado', sa.DateTime(), nullable=True),
    sa.Column('atleta_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['atleta_id'], ['atleta.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('historicocompeticao',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('data_competicao', sa.Date(), nullable=False),
    sa.Column('jogos_completos', sa.Integer(), nullable=False),
    sa.Column('jogos_parciais', sa.Integer(), nullable=False),
    sa.Column('minutagem', sa.Integer(), nullable=False),
    sa.Column('gols', sa.Integer(), nullable=False),
    sa.Column('assistencias', sa.Integer(), nullable=False),
    sa.Column('data_criacao', sa.DateTime(), nullable=False),
    sa.Column('data_atualizado', sa.DateTime(), nullable=True),
    sa.Column('atleta_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['atleta_id'], ['atleta.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('historicocontrole',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('quantidade', sa.Integer(), nullable=False),
    sa.Column('preco', sa.Float(), nullable=False),
    sa.Column('data_controle', sa.Date(), nullable=False),
    sa.Column('data_criacao', sa.DateTime(), nullable=False),
    sa.Column('data_atualizado', sa.DateTime(), nullable=True),
    sa.Column('atleta_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['atleta_id'], ['atleta.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('historicolesao',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('data_lesao', sa.Date(), nullable=False),
    sa.Column('descricao', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('data_retorno', sa.Date(), nullable=True),
    sa.Column('data_criacao', sa.DateTime(), nullable=False),
    sa.Column('data_atualizado', sa.DateTime(), nullable=True),
    sa.Column('atleta_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['atleta_id'], ['atleta.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('historicoobservacao',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tipo', sa.Enum('desempenho', 'relacionamento', name='obsevacaotypes'), nullable=True),
    sa.Column('descricao', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('data_criacao', sa.DateTime(), nullable=False),
    sa.Column('atleta_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['atleta_id'], ['atleta.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('relacionamento',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('receptividade_contrato', sa.Integer(), nullable=False),
    sa.Column('satisfacao_empresa', sa.Integer(), nullable=False),
    sa.Column('satisfacao_clube', sa.Integer(), nullable=False),
    sa.Column('relacao_familiares', sa.Integer(), nullable=False),
    sa.Column('influencias_externas', sa.Integer(), nullable=False),
    sa.Column('pendencia_empresa', sa.Boolean(), nullable=False),
    sa.Column('pendencia_clube', sa.Boolean(), nullable=False),
    sa.Column('data_avaliacao', sa.Date(), nullable=False),
    sa.Column('data_criacao', sa.DateTime(), nullable=False),
    sa.Column('data_atualizado', sa.DateTime(), nullable=True),
    sa.Column('atleta_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['atleta_id'], ['atleta.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('rolepermissao',
    sa.Column('role_id', sa.Integer(), nullable=False),
    sa.Column('permissao_id', sa.Integer(), nullable=False),
    sa.Column('data_criacao', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['permissao_id'], ['permissao.id'], ),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
    sa.PrimaryKeyConstraint('role_id', 'permissao_id')
    )
    op.create_table('usuario',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('hash_password', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('data_criacao', sa.DateTime(), nullable=False),
    sa.Column('data_atualizado', sa.DateTime(), nullable=True),
    sa.Column('usuario_tipo_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['usuario_tipo_id'], ['usuariotipo.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('contrato',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('data_inicio', sa.Date(), nullable=False),
    sa.Column('data_termino', sa.Date(), nullable=False),
    sa.Column('observacao', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('versao', sa.Integer(), nullable=False),
    sa.Column('ativo', sa.Boolean(), nullable=False),
    sa.Column('data_criacao', sa.DateTime(), nullable=False),
    sa.Column('data_atualizado', sa.DateTime(), nullable=True),
    sa.Column('atleta_id', sa.Integer(), nullable=False),
    sa.Column('contrato_sub_tipo_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['atleta_id'], ['atleta.id'], ),
    sa.ForeignKeyConstraint(['contrato_sub_tipo_id'], ['contratosubtipo.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('usuariopermissao',
    sa.Column('usuario_id', sa.Integer(), nullable=False),
    sa.Column('permissao_id', sa.Integer(), nullable=False),
    sa.Column('data_criacao', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['permissao_id'], ['permissao.id'], ),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuario.id'], ),
    sa.PrimaryKeyConstraint('usuario_id', 'permissao_id')
    )
    op.create_table('usuariorole',
    sa.Column('usuario_id', sa.Integer(), nullable=False),
    sa.Column('role_id', sa.Integer(), nullable=False),
    sa.Column('data_criacao', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuario.id'], ),
    sa.PrimaryKeyConstraint('usuario_id', 'role_id')
    )
    op.create_table('contratoversao',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('versao', sa.Integer(), nullable=False),
    sa.Column('data_inicio', sa.Date(), nullable=False),
    sa.Column('data_termino', sa.Date(), nullable=False),
    sa.Column('observacao', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('data_criacao', sa.DateTime(), nullable=False),
    sa.Column('data_atualizado', sa.DateTime(), nullable=True),
    sa.Column('contrato_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['contrato_id'], ['contrato.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('contratoversao')
    op.drop_table('usuariorole')
    op.drop_table('usuariopermissao')
    op.drop_table('contrato')
    op.drop_table('usuario')
    op.drop_table('rolepermissao')
    op.drop_table('relacionamento')
    op.drop_table('historicoobservacao')
    op.drop_table('historicolesao')
    op.drop_table('historicocontrole')
    op.drop_table('historicocompeticao')
    op.drop_table('historicoclube')
    op.drop_table('contratosubtipo')
    op.drop_table('caracteristicazagueiro')
    op.drop_table('caracteristicavolante')
    op.drop_table('caracteristicameia')
    op.drop_table('caracteristicalateral')
    op.drop_table('caracteristicagoleiro')
    op.drop_table('caracteristicafisica')
    op.drop_table('caracteristicaatacante')
    op.drop_table('caracteristica')
    op.drop_table('atletavideos')
    op.drop_table('atletaposicao')
    op.drop_table('atletaimagens')
    op.drop_table('atletaavatar')
    op.drop_table('usuariotipo')
    op.drop_table('role')
    op.drop_table('posicao')
    op.drop_table('permissao')
    op.drop_table('perfil')
    op.drop_table('contratotipo')
    op.drop_table('atleta')
    # ### end Alembic commands ###
