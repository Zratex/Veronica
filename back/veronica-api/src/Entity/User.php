<?php

namespace App\Entity;

use ApiPlatform\Metadata\ApiResource;
use App\Repository\UserRepository;
use Doctrine\DBAL\Types\Types;
use Doctrine\ORM\Mapping as ORM;

#[ORM\Entity(repositoryClass: UserRepository::class)]
#[ORM\Table(name: '`user`')]
#[ApiResource]
class User
{
    #[ORM\Id]
    #[ORM\Column(type: Types::TEXT)]
    private ?string $id_discord = null;

    #[ORM\Column(type: Types::TEXT, nullable: true)]
    private ?string $username = null;

    #[ORM\Column(nullable: true)]
    private ?int $money = null;

    #[ORM\Column(type: Types::DATETIME_MUTABLE)]
    private ?\DateTimeInterface $creation_date = null;

    #[ORM\Column(type: Types::DATETIME_MUTABLE, nullable: true)]
    private ?\DateTimeInterface $daily_cooldown = null;

    #[ORM\Column]
    private ?int $xp = null;

    #[ORM\Column]
    private ?int $stock_conchiglie = null;

    #[ORM\Column]
    private ?int $stock_lootbox = null;

    #[ORM\ManyToOne(targetEntity: Levels::class)]
    #[ORM\JoinColumn(name: 'id_levels', referencedColumnName: 'level', nullable: false, columnDefinition: 'INT DEFAULT 0')]
    #[ORM\Column]
    private ?int $level = null;

    public function getUsername(): ?string
    {
        return $this->username;
    }

    public function getIdDiscord(): ?string
    {
        return $this->id_discord;
    }

    public function setUsername(string $username): static
    {
        $this->username = $username;

        return $this;
    }

    public function getMoney(): ?int
    {
        return $this->money;
    }

    public function setMoney(?int $money): static
    {
        $this->money = $money;

        return $this;
    }

    public function getCreationDate(): ?\DateTimeInterface
    {
        return $this->creation_date;
    }

    public function setCreationDate(\DateTimeInterface $creation_date): static
    {
        $this->creation_date = $creation_date;

        return $this;
    }

    public function getDailyCooldown(): ?\DateTimeInterface
    {
        return $this->daily_cooldown;
    }

    public function setDailyCooldown(?\DateTimeInterface $daily_cooldown): static
    {
        $this->daily_cooldown = $daily_cooldown;

        return $this;
    }

    public function getXp(): ?int
    {
        return $this->xp;
    }

    public function setXp(int $xp): static
    {
        $this->xp = $xp;

        return $this;
    }

    public function getStockConchiglie(): ?int
    {
        return $this->stock_conchiglie;
    }

    public function setStockConchiglie(int $stock_conchiglie): static
    {
        $this->stock_conchiglie = $stock_conchiglie;

        return $this;
    }

    public function getStockLootbox(): ?int
    {
        return $this->stock_lootbox;
    }

    public function setStockLootbox(int $stock_lootbox): static
    {
        $this->stock_lootbox = $stock_lootbox;

        return $this;
    }

    public function getLevel(): ?int
    {
        return $this->level;
    }

    public function setLevel(int $level): static
    {
        $this->level = $level;

        return $this;
    }
}
