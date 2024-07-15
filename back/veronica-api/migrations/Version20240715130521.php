<?php

declare(strict_types=1);

namespace DoctrineMigrations;

use Doctrine\DBAL\Schema\Schema;
use Doctrine\Migrations\AbstractMigration;

/**
 * Auto-generated Migration: Please modify to your needs!
 */
final class Version20240715130521 extends AbstractMigration
{
    public function getDescription(): string
    {
        return '';
    }

    public function up(Schema $schema): void
    {
        $this->addSql('DROP SCHEMA IF EXISTS public CASCADE');
        $this->addSql('CREATE SCHEMA public');
        $this->addSql('DROP SEQUENCE IF EXISTS apilog_id_seq CASCADE');
        $this->addSql('DROP SEQUENCE IF EXISTS levels_id_seq CASCADE');
        $this->addSql('DROP SEQUENCE IF EXISTS "user_id_seq" CASCADE');
        $this->addSql('DROP TABLE IF EXISTS apilog');
        $this->addSql('DROP TABLE IF EXISTS levels');
        $this->addSql('DROP TABLE IF EXISTS "user"');
        // this up() migration is auto-generated, please modify it to your needs
        $this->addSql('CREATE SEQUENCE apilog_id_seq INCREMENT BY 1 MINVALUE 1 START 1');
        $this->addSql('CREATE SEQUENCE levels_id_seq INCREMENT BY 1 MINVALUE 1 START 1');
        $this->addSql('CREATE SEQUENCE "user_id_seq" INCREMENT BY 1 MINVALUE 1 START 1');
        $this->addSql('CREATE TABLE apilog (id INT NOT NULL, apilog_id INT NOT NULL, origin TEXT NOT NULL, method TEXT NOT NULL, route TEXT NOT NULL, time TIMESTAMP(0) WITHOUT TIME ZONE NOT NULL, PRIMARY KEY(id))');
        $this->addSql('CREATE TABLE levels (id INT NOT NULL, level INT NOT NULL, xp_required INT NOT NULL, role_name TEXT NOT NULL, PRIMARY KEY(id))');
        $this->addSql('CREATE TABLE "user" (id INT NOT NULL, username TEXT DEFAULT NULL, id_discord TEXT NOT NULL, money INT DEFAULT NULL, creation_date TIMESTAMP(0) WITHOUT TIME ZONE NOT NULL, daily_cooldown TIMESTAMP(0) WITHOUT TIME ZONE DEFAULT NULL, xp INT NOT NULL, stock_conchiglie INT NOT NULL, stock_lootbox INT NOT NULL, level INT NOT NULL, PRIMARY KEY(id))');
    }

    public function down(Schema $schema): void
    {
        // this down() migration is auto-generated, please modify it to your needs
        $this->addSql('CREATE SCHEMA public');
    }
}
